## To run server: python llm_server.py
## To run client: python llm_chat.py

import requests

url = "http://127.0.0.1:5000/"
#url = "https://2488-34-147-72-197.ngrok-free.app/"

url = url + "text/"

while True:
   prompt = input("<You>: ")
   r = requests.post(url, json={'text': prompt})
   print()
   print("<LLM>: "+r.text)
