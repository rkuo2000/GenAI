#!/usr/bin/env python3
"""
MATLAB MCP Client - Connect to MATLAB/Octave MCP server for Claude Desktop
"""

import subprocess
import json
import sys
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    server_script = os.path.join(script_dir, "matlab_mcp_server.m")
    
    print("Starting MATLAB/Octave MCP Server...")
    print(f"Script path: {server_script}")
    print()
    print("Add the following to your Claude Desktop config (~/.claude-desktop.json):")
    print()
    print(json.dumps({
        "mcpServers": {
            "matlab": {
                "command": sys.executable,
                "args": [os.path.abspath(__file__)]
            }
        }
    }, indent=2))
    print()
    print("Press Ctrl+C to stop this server.")
    
    try:
        subprocess.run([
            "octave", "--eval", 
            f"addpath('{server_script}'); MCPServer().start();"
        ], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except FileNotFoundError:
        print("Error: Octave not found. Please install Octave or update the PATH.")
        sys.exit(1)


if __name__ == "__main__":
    main()
