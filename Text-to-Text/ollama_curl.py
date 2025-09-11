import requests

#url = "http://127.0.0.1:11434"
url = "http://106.1.125.187:11434"

jsondata = {
    "model":'gemma3',
    "prompt": "請列出五樣台灣美食",
    "stream": False,
    "options": {
        "seed": 123,
        "top_k": 20,
        "top_p": 0.9,
        "temperature": 0
    }
}

r = requests.post(url+"/api/generate", json=jsondata)
outputs = r.json()
print(outputs["response"])
