# MATLAB MCP Server for Claude Desktop

A Model Context Protocol (MCP) server that provides MATLAB/Octave control system tools for Claude.

## Files

- `matlab_mcp_server.m` - MATLAB/Octave class implementing the MCP server
- `run_matlab_mcp.py` - Python wrapper for easy launching
- `matlab_mcp_client.py` - Direct client script

## Setup

### 1. Prerequisites

- **Octave** (recommended - free) or **MATLAB**
- Python 3.8+ (for the wrapper script)

### 2. Install Octave (if needed)

**Windows:**
```powershell
winget install GNU.Octave
```

**macOS:**
```bash
brew install octave
```

**Linux:**
```bash
sudo apt install octave  # Debian/Ubuntu
sudo dnf install octave  # Fedora
```

### 3. Configure Claude Desktop

Add to `~/.claude-desktop.json`:

```json
{
  "mcpServers": {
    "matlab": {
      "command": "python",
      "args": ["C:/Users/User/coding/current-control/run_matlab_mcp.py"]
    }
  }
}
```

Or use Octave directly:

```json
{
  "mcpServers": {
    "matlab": {
      "command": "octave",
      "args": ["--eval", "addpath('C:/Users/User/coding/current-control'); MCPServer().start();"]
    }
  }
}
```

## Available Tools

### matlab_eval
Evaluate any MATLAB/Octave expression.

### matlab_workspace
List all variables in the workspace.

### matlab_load / matlab_save
Load/save .mat files.

### matlab_plot
Create plots (plot, scatter, bar, stem).

### matlab_control_sim
Simulate control system step/impulse response.

### matlab_pid_tune
Design and simulate PID controllers.

### matlab_bode
Generate Bode plot data with margins.

### matlab_nyquist
Generate Nyquist plot data.

### matlab_lsim
Simulate linear system to arbitrary input.

## Usage Examples

```
You: Design a PID controller for a plant G(s) = 1/(s^2 + s + 1)
Claude: [Uses matlab_pid_tune to design and simulate]
```

```
You: Plot the step response of a 2nd order system
Claude: [Uses matlab_control_sim with plot generation]
```

```
You: Calculate the Bode plot for a transfer function
Claude: [Uses matlab_bode to analyze frequency response]
```
