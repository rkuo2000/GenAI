# ollama run llama3 (on GPU)

import requests

url = "http://127.0.0.1:11434"
#url = "http://123.195.32.57:11434"
#url = "http://5acc-34-124-174-25.ngrok-free.app:11434"
url = url + "/api/chat"

prompt = input("<You>: ")
jsondata = {
  "model": "llava-llama3",
  "messages": [
    {
      "role": "user",
      "content": prompt
    }
  ],
  "stream": False
}

r = requests.post(url, json=jsondata)
outputs = r.json()
print("<LLM>: "+outputs["message"]["content"])
