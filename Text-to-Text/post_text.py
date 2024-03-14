## To run server: python whisper_server.py
## To run client: python post_audio.py

import requests

url = "http://127.0.0.1:8000/text"
#url = "http://123.195.32.57:8000/text"

prompt = "how are you?"
r = requests.post(url, json={'text': prompt})

print(r.json())
