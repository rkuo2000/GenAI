## To run server: python llm_server.py
## To run client: python llm_chat.py

import requests

url = "http://127.0.0.1:5000/"
#url = "http://123.195.32.57:5000/"
#url = "https://400e-34-173-108-154.ngrok-free.app/"

url = url + "text/"

while True:
   prompt = input("<You>: ")
   r = requests.post(url, json={'text': prompt})
   print()
   print("<LLM>: "+r.text)
