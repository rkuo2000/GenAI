# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY="get_it_from" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open("images/test.jpg")
prompt = "Can you tell me about this photo?"

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content( [prompt , img] )
print(result.text)
