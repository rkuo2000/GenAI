## To run server: python llm_server.py
## To run client: python post_text.py

import requests

url = "http://127.0.0.1:5000/text/"

#prompt = "How are you?"
#prompt = "Please make me a coffee"
prompt = "請為我煮一杯咖啡"

r = requests.post(url, json={'text': prompt})

print(r.text)
