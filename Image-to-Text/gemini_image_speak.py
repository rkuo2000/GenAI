# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
from gtts import gTTS
import os

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key, transport='rest')

img = PIL.Image.open("images/test.jpg")
prompt = "Can you tell me about this photo? simple description in traditional chinese"

model = genai.GenerativeModel("gemini-2.0-flash-exp")

result = model.generate_content( [prompt , img] )
print(result.text)

## TTS
tts = gTTS(result.text, lang="zh-TW")
tts.save("gTTS.mp3")

## Speak
os.system("mpg123 -q gTTS.mp3")
