## To run server: python whisper_server.py
## To run client: python post_audio.py

import requests

url = "http://127.0.0.1:8000/audio"

#my_audio = {'audio': open("audio1.flac", "rb")}
#my_audio = {'audio': open("audio2.mp3", "rb")}
my_audio = {'audio': open("audio3.mp4", "rb")}

r = requests.post(url, files=my_audio)

print(r.json())
