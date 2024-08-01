import requests

url = "http://127.0.0.1:11434"
url = url + "/api/generate"

jsondata = {
#    model='snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0', # TAIDE
#    model='llama3.1',
#    model='tinyllama',
    model='gemma2:2b',
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
