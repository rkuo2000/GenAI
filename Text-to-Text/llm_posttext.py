## To run server: python llm_server.py
## To run client: python llm_posttext.py "why is the sky blue?"

import requests
import sys

url = "http://127.0.0.1:5000"
#url = "http://123.195.32.57:5000"
#url = "https://6eef-35-230-18-109.ngrok-free.app"

url = url + "/text/"

prompt = sys.argv[1]
r = requests.post(url, json={'text': prompt})
print()
print("<LLM>: "+r.text)
