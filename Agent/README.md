
# [Agent](https://rkuo2000.github.io/AI-course/lecture/2025/09/13/Agents.html)

---
## Local LLM

### llama-cpp-python

### install [Ollama](https://ollama.com/search)
`curl -fsSL https://ollama.com/install.sh | sh` <br>
`ollama -v` <br>
`ollama pull gpt-oss:latest` <br>
`ollama list`<br>
`ollama run gpt-oss:latest` <br>
**API:** `http://127.0.0.1:11434/v1`<br>

---
### setup Ollama service
`sudo nano /etc/systemd/system/ollama.service` <br>

#### to run with multiple GPUs
```
Environment="OLLAMA_SCHED_SPREAD=1"
Environment="CUDA_VISIBLE_DEVICES=1,0"
```

---
### set Ollama debugging 

#### to run with DEBUG level 2
```
Environment="OLLAMA_DEBUG=2"
```

#### restart Ollama service
`sudo systemctl daemon-reload` <br>
`sudo systemctl restart ollama` <br>

#### monitor Ollama debug message
`journalctl -f -b -u ollama` <br> 

---
## Agentic Coding Tools

### [Claud-code](https://github.com/anthropics/claude-code)
**Install**: `curl -fsSL https://claude.ai/install.sh | bash` <br>

---
### [OpenCode](https://github.com/anomalyco/opencode)
**Install**: `curl -fsSL https://opencode.ai/install | bash` <br>

![](https://github.com/anomalyco/opencode/raw/dev/packages/web/src/assets/lander/screenshot.png)

**OpenCode setup** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/8toBNmRDO90)](https://youtu.be/8toBNmRDO90)
[![](https://markdown-videos-api.jorgenkh.no/youtube/JYVTUU9ClUA)](https://youtu.be/JYVTUU9ClUA)

---
## CLI

### [gws](https://github.com/googleworkspace/cli)
**Install**: `npm install -g @googleworkspace/cli`<br>

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
## Personal Agent

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*yWZcgi24bHe3AZOevKpWmQ.png)

### [OpenClaw](https://github.com/openclaw/openclaw)
OpenClaw is a personal AI assistant you run on your own devices

### [NanoClaw](https://github.com/qwibitai/nanoclaw) 
An AI assistant that runs agents securely in their own containers.

### [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) - run on $10 hardware
ZeroClaw is the runtime operating system for agentic workflows 

### [PicoClaw](https://github.com/sipeed/picoclaw) 
🦐 PicoClaw is an ultra-lightweight personal AI Assistant inspired by nanobot

### [MimiClaw](https://github.com/memovai/mimiclaw)
Pocket AI Assistant on a $5 Chip

**Blog**: [mimiClaw](https://www.cnx-software.com/2026/02/13/mimiclaw-is-an-openclaw-like-ai-assistant-for-esp32-s3-boards/)<br>


