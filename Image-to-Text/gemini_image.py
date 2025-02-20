# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY="paste_api_key_here" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY, transport='rest')

img = PIL.Image.open("images/test_big_data.png")
#prompt = "Can you tell me about this photo?" + "please answer in traditional chinese"
#prompt = "請問這張照片的內容有什麼?"
prompt = "請問前三名跟佳作總共可獲得多少錢?"

model = genai.GenerativeModel("gemini-2.0-flash")
#model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")

result = model.generate_content( [prompt , img] )
print(result.text)
