## OpenClaw ~ Personal Assistant

### OpenClaw Architecture
![](https://help.apiyi.com/wp-content/uploads/2026/01/clawdbot-beginner-guide-personal-ai-assistant-2026-fr-image-1.png)

**Blog**: [OpenClaw (Clawdbot) Architecture: Engineering Reliable and Controllable AI Agents](https://vertu.com/ai-tools/openclaw-clawdbot-architecture-engineering-reliable-and-controllable-ai-agents/)<br>

---
### install node & npm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install node
```

* `node -v`
v25.9.0

* `npm -v`
v 11.12.1

---
### OpenClaw setup

#### install [OpenClaw](https://github.com/openclaw/openclaw)
1. `sudo npm install -g openclaw@latest`
2. `openclaw -v`
3. `openclaw onboard --install-daemon`
4. `openclaw gateway restart`
5. open browser `http://127.0.0.1:18789`

[.openclaw/openclaw.json](https://github.com/rkuo2000/GenAI/blob/main/Agent/openclaw.json)<br>

---
#### setup Ollama
add the following into `~/.openclaw/openclaw.json` <br>
```
  "models": {
    "mode": "merge",
    "providers": {
      "ollama": {
        "baseUrl": "http://127.0.0.1:11434/v1",
        "apiKey": "ollama",
        "api": "openai-responses",
        "models": [
          {
            "id": "gemma4-e2b:latest",
            "name": "Gemma4:e2b (Local)",
            "modalities": { "input": ["text", "image"], "output": ["text"] },
            "reasoning": false,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "contextWindow": 32768,
            "maxTokens": 4096
          }
        ]
      }
    }
```

To access a remote Ollama server: <br>
* modify openclaw.json, *replace `127.0.0.1` to `192.168.0.12` (remote ip addr)* 
* modify ufw rules on Ollama server, *`sudo ufw allow from 192.168.0.22`*

---
#### setup WhatsApp
*.openclaw/openclaw.json*<br>
```
  "channels": {
    "whatsapp": {
      "selfChatMode": true,
      "dmPolicy": "allowlist",
      "allowFrom": [
        "+886972123456"
      ]
    }
  },
```

---
#### setup Firewall
```
sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow in on tailscale0 to any port 22
sudo ufw enable #Type 『y』 to confirm`
sudo ufw status
```
