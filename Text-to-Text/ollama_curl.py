# ollama run llama3.1

import requests

url = "http://127.0.0.1:11434"
url = url + "/api/generate"

jsondata = {
  "model": "llama3.1",
  "prompt": "請列出五樣台灣美食",
  "stream": False,
  "options": {
      "seed": 123,
      "top_k": 20,
      "top_p": 0.9,
      "temperature": 0
      }
}

r= requests.post(url, json=jsondata)
outputs = r.json()
print(outputs["response"])
