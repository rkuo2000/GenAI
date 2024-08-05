#!/home/user/venv/bin/python

import google.generativeai as genai
import PIL.Image
import os
from gtts import gTTS

sl = "zh-TW"

GOOGLE_API_KEY="AIzaSyCnRzbxgrMX1GjIHnN7U6EQVM8YKy9Ikw4" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open("out.jpg")
prompt = "Can you tell me about this photo? simple description in traditional chinese."

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content( [prompt , img] )
print(result.text)

tts=gTTS(result.text, lang=sl)
tts.save("gTTS.mp3")
os.system("mpg123 -q gTTS.mp3")

