## To run client: python post_text.py

import requests

#url = "http://127.0.0.1:5000"
#url = "http://123.195.32.57:5000"
url = "https://8f62-34-105-42-193.ngrok-free.app" # server on Colab
url = url + "/text"

prompt = "Hello, How are you?"
#prompt = "Could you make me a coffee?"
#prompt = "Why is the sky blue?"
#prompt = "早安你好"
#prompt = "台灣第一高山是什麼山?"
#prompt = "你是一個人形機器人, 請煮一杯咖啡給我, 並一步一步解釋你的動作"

r = requests.post(url, json={'text': prompt})

print(r.text)
