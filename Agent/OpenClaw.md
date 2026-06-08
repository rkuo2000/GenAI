## Personal Agent

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
### install node & npm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install node
```

* `node -v`
v25.6.1

* `npm -v`
v 11.9.0

* `npm install -g npm@latest`
v 11.10.0

---
### install brew
`sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"`<br>

```
test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bashrc
```

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
            "id": "gpt-oss:latest",
            "name": "GPT-OSS:20b (Local)",
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
* modify ufw rules on Ollama server, *`sudo ufw allow from 192.168.0.18`*

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
#### setup Gmail
* **API和服務**
  - **建立專案** [Google Console && create project](https://console.cloud.google.com/projectcreate)
  - **專案名稱** `Openclaw-Gmail-API`
* **API和服務** ==> **+啟用API和服務** ==> **[Gmail API]** ==> Enable
* **憑證** ==> **建立憑證** ==> **OAuth用戶端ID**
  - **應用程式類型** : 選`電腦版應用程式`
  - **名稱** : 填`OpenClaw` ==> 按`建立` ==> 下載JSON
  - 下載後改名 `client_secret.json` 移至`.openclaw/workspace`
* 在`localhost:18789`, prompt輸入 `read .openclaw/workspace/client_secret.json and make a gmail-auth.py to access Gmail API`
* 自動會在workspace中產生 gmail_auth.py
* `pip install --upgrade google-auth-oauthlib google-auth-httplib2`
* `python gmail-auth.py`
* 執行後會開啟瀏覽器，選定Gmail帳號，按**繼續** 即可完成授權。
  
---
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

---
#### Multiple Agents
[![](https://markdown-videos-api.jorgenkh.no/youtube/masJoPqT-6A)](https://youtu.be/masJoPqT-6A)
