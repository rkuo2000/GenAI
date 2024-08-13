## To run client: python get_text.py

import requests
import json

url = "http://123.195.32.57:5000"
url = url + "/query/"

prompt = "區權會多久需要召開一次"

r = requests.get(url+prompt)
print("Ans: ")
print(r.text)
