
# [Agent](https://rkuo2000.github.io/AI-course/lecture/2025/09/13/Agents.html)

---
## Local LLM

### [Ollama](https://ollama.com/search)
`curl -fsSL https://ollama.com/install.sh | sh` <br>
`ollama -v` <br>
`ollama pull gpt-oss:latest` <br>
`ollama list`<br>
`ollama run gpt-oss:latest` <br>
**API:** `http://127.0.0.1:11434/v1`<br>

---
### [LM Studio](https://lmstudio.ai/)
![](https://github.com/rkuo2000/GenAI/blob/main/assets/LM_studio_server.png?raw=true)

---
## Vibe Coding

### [AntiGravity](https://antigravity.google/)
* **[Getting-Started](https://antigravity.google/docs/get-started)**
* **[Agent Modes / Settings](https://antigravity.google/docs/agent-modes-settings)**

---
## Agentic AI coding tools

### [Claud-code](https://github.com/anthropics/claude-code)
**Install**: `curl -fsSL https://claude.ai/install.sh | bash` <br>

![](https://github.com/anthropics/claude-code/raw/main/demo.gif)

---
### [OpenCode](https://github.com/anomalyco/opencode)
**Install**: `npm i -g opencode-ai@latest` <br>

![](https://github.com/anomalyco/opencode/raw/dev/packages/web/src/assets/lander/screenshot.png)

**OpenCode setup: Beginner’s Crash course** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/8toBNmRDO90)](https://youtu.be/8toBNmRDO90)

**OpenCode詳細攻略** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/JYVTUU9ClUA)](https://youtu.be/JYVTUU9ClUA)

---
### [MCP-Servers](https://modelcontextprotocol.io/docs/getting-started/intro)

* [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server)

**OpenCode最强插件** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/twFjLiy2Pmc)](https://youtu.be/twFjLiy2Pmc)

---
### [Skills](https://code.claude.com/docs/en/skills)

**爆火的Skills怎麼用？** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/3nm_hDALBmY)](https://youtu.be/3nm_hDALBmY)

---
## Personal AI Agent

### OpenClaw Architecture
![](https://help.apiyi.com/wp-content/uploads/2026/01/clawdbot-beginner-guide-personal-ai-assistant-2026-fr-image-1.png)

**Blog**: [OpenClaw (Clawdbot) Architecture: Engineering Reliable and Controllable AI Agents](https://vertu.com/ai-tools/openclaw-clawdbot-architecture-engineering-reliable-and-controllable-ai-agents/)<br>

The 6-Stage Execution Pipeline:<br>
1. **Channel Adapter**: Standardizes inputs from different platforms (e.g., Discord or Telegram) into a unified message format while extracting necessary attachments.
2. **Gateway Server**: Acts as a session coordinator, determining which session a message belongs to and assigning it to the appropriate queue.
3. **Lane Queue**: A critical reliability layer that enforces serial execution by default, allowing parallelism only for explicitly marked low-risk tasks.
4. **Agent Runner**: The “assembly line” for the model. It handles model selection, API key cooling, prompt assembly, and context window management.
5. **Agentic Loop**: The iterative cycle where the model proposes a tool call, the system executes it, the result is backfilled, and the loop continues until a resolution is reached or limits are hit.
6. **Response Path**: Streams final content back to the user channel while simultaneously writing the entire process to a JSONL transcript for auditing and replay.

---
### OpenClaw Installation
[![](https://markdown-videos-api.jorgenkh.no/youtube/daXOXSSyudM)](https://youtu.be/daXOXSSyudM)

#### setup VPN : Tailscale
```
curl -fsSL <https://tailscale.com/install.sh> | sh
sudo tailscale up
```

#### setup Firewall
```
sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow in on tailscale0 to any port 22
sudo ufw enable #Type 『y』 to confirm`
sudo ufw status
```

#### install [OpenClaw](https://github.com/openclaw/openclaw)
1. `npm install -g openclaw@latest` <br>
2. `openclaw onboard --install-daemon` <br>
3. `openclaw gateway restart` <br>
4. open browser `http://127.0.0.1:18789` <br>

[.openclaw/openclaw.json](https://github.com/rkuo2000/GenAI/blob/main/Agent/openclaw.json)<br>

#### Multiple Agents
[![](https://markdown-videos-api.jorgenkh.no/youtube/masJoPqT-6A)](https://youtu.be/masJoPqT-6A)
