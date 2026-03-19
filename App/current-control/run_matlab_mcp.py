#!/usr/bin/env python3
import subprocess
import sys
import json
import threading
import time

class MATLABMCPServer:
    def __init__(self, matlab_path: str | None = None, octave_path: str | None = None):
        self.matlab_path = matlab_path or "matlab"
        self.octave_path = octave_path or "octave"
        self.process: subprocess.Popen | None = None
        self.running = False
    
    def start_octave(self, script_path, port=None):
        try:
            self.process = subprocess.Popen(
                [self.octave_path, "--eval", f"addpath('{script_path}'); MCPServer().start();"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            self.running = True
            return True
        except FileNotFoundError:
            print(f"Error: {self.octave_path} not found. Install Octave or update path.", file=sys.stderr)
            return False
    
    def start_matlab(self, script_path):
        try:
            self.process = subprocess.Popen(
                [self.matlab_path, "-batch", f"addpath('{script_path}'); MCPServer().start();"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            self.running = True
            return True
        except FileNotFoundError:
            print(f"Error: {self.matlab_path} not found. Install MATLAB or update path.", file=sys.stderr)
            return False
    
    def send_request(self, method, params=None, id=None):
        proc: subprocess.Popen = self.process  # type: ignore[assignment]
        if not proc:
            return
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
        }
        if id is not None:
            request["id"] = id
        
        request_str = json.dumps(request)
        proc.stdin.write(request_str + "\n")  # type: ignore[union-attr]
        proc.stdin.flush()  # type: ignore[union-attr]
        
        if method == "shutdown":
            self.running = False
    
    def read_response(self, timeout=5):
        proc: subprocess.Popen = self.process  # type: ignore[assignment]
        if not proc:
            return None
        start = time.time()
        while time.time() - start < timeout:
            line = proc.stdout.readline()  # type: ignore[union-attr]
            if line:
                return json.loads(line.strip())
        return None
    
    def call_tool(self, tool_name, arguments=None):
        self.send_request("tools/call", {
            "name": tool_name,
            "arguments": arguments or {}
        })
        return self.read_response()
    
    def list_tools(self):
        self.send_request("tools/list")
        return self.read_response()
    
    def stop(self):
        if self.process:
            self.send_request("shutdown")
            self.process.wait(timeout=5)
            self.running = False
    
    def run(self, script_path, use_octave=True):
        if use_octave:
            success = self.start_octave(script_path)
        else:
            success = self.start_matlab(script_path)
        
        if not success:
            return False
        
        self.send_request("initialize")
        resp = self.read_response()
        if resp and "result" in resp:
            print(f"Connected to {resp['result']['serverInfo']['name']} v{resp['result']['serverInfo']['version']}")
        
        return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="MATLAB MCP Server Runner")
    parser.add_argument("--matlab", type=str, help="Path to MATLAB executable")
    parser.add_argument("--octave", type=str, help="Path to Octave executable")
    parser.add_argument("--script-path", type=str, default=".", help="Path to matlab_mcp_server.m")
    parser.add_argument("--use-octave", action="store_true", default=True, help="Use Octave (default)")
    parser.add_argument("--use-matlab", action="store_true", help="Use MATLAB instead of Octave")
    args = parser.parse_args()
    
    server = MATLABMCPServer(
        matlab_path=args.matlab,
        octave_path=args.octave
    )
    
    use_octave = not args.use_matlab
    
    if server.run(args.script_path, use_octave=use_octave):
        print("MCP Server running. Press Ctrl+C to stop.")
        try:
            while server.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down...")
            server.stop()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
