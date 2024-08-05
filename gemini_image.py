# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY="get_api_key_from" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open("images/test.jpg")
#prompt = "Can you tell me about this photo? simple description in traditional chinese"
prompt = "Can you tell me about this photo? answer in traditional chinese"

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content( [prompt , img] )
print(result.text)
