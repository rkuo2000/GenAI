# ollama run llama3

import requests

url = "http://127.0.0.1:11434"
url = url + "/api/chat"

prompt = input("<You>: ")
jsondata = {
  "model": "llama3",
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
