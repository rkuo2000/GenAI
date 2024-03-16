## To run server: python llm_server.py
## To run client: python post_text.py

import requests

url = "http://127.0.0.1:5000/text/"
#url = "https://6981-104-199-160-98.ngrok-free.app/text"

#prompt = "How are you?"
#prompt = "could you make me a coffee"
prompt = "請為我煮一杯咖啡"

r = requests.post(url, json={'text': prompt})

print(r.text)
