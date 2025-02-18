# pip install google.generativeai

import os
import pathlib
import google.generativeai as genai
from google.generativeai import types

GOOGLE_API_KEY="  " ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

audio = {"mime_type": "audio/mp3", "data":pathlib.Path("gTTS.mp3").read_bytes()}
prompt = 'please transcribe this audio clip'

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content([prompt, audio])

print(response.text)
