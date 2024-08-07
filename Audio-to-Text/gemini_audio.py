# pip install google.generativeai

import google.generativeai as genai
import pathlib
import os

GOOGLE_API_KEY="get_it_from" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

audio = {"mime_type": "audio/mp3", "data":pathlib.Path("test.mp3").read_bytes()}
#prompt = "Please summarize the audio."
prompt = "Please convert the audio to text."

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content([prompt, audio])
print(result.text)
