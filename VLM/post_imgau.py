## To run server: python whisper_llava_server.py
## To run client: python post_imgau.py

import requests

url = "http://127.0.0.1:5000/multi/"

##TTS: python ../gTTS.py "What are the things I should be cautious about when I visit this place?" en  
#image = requests.get("https://llava-vl.github.io/static/images/view.jpg", stream=True).raw

##TTS: python ../gTTS.py "這是什麼有名的台南美食?" zh
image = open("images/Tainan_BeefSoup.jpg", "rb")

##TTS: python ../gTTS.py "這是什麼著名的基隆景點" zh
#image = open("images/daping_coast.jpg", "rb")

audio = open("gTTS.mp3", "rb")

multi_files = [('image', ('test.jpg', image, 'image/jpeg')),
               ('audio', ('gTTS.mp3', audio, 'audio/mpeg')) ]
r = requests.post(url, files=multi_files)

print(r.text)
