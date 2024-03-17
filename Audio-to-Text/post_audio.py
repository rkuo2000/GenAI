## To run server: python whisper_server.py
## To run client: python post_audio.py

import requests

url = "http://127.0.0.1:5000/audio"
#url = "http://123.195.32.57:5000/audio"
#url = "https://3590-34-143-234-224.ngrok-free.app/audio"

#my_audio = {'audio': open("audio1.flac", "rb")}
#my_audio = {'audio': open("audio2.mp3", "rb")}
#my_audio = {'audio': open("audio3.mp4", "rb")}
#my_audio = {'audio': open("hello_howareyou.mp4", "rb")}
my_audio = {'audio': open("gTTS.mp3", "rb")}

r = requests.post(url, files=my_audio)
print(r.text)
