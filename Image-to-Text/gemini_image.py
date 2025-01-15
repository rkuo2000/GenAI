# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY="get_it_from" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY, transport='rest')

img = PIL.Image.open("images/test.jpg")
#prompt = "Can you tell me about this photo?"
prompt = "你在這張照片看到了什麼?"

model = genai.GenerativeModel("gemini-2.0-flash-exp")

result = model.generate_content( [prompt , img] )
print(result.text)
