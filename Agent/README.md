
# [Agent](https://rkuo2000.github.io/AI-course/lecture/2025/09/13/Agents.html)

---
## Local LLM

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
### [LM Studio](https://lmstudio.ai/)

---
## Agentic Coding Tools

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
## Personal Agent

### [OpenClaw](https://github.com/rkuo2000/GenAI/blob/main/Agent/OpenClaw.md)


