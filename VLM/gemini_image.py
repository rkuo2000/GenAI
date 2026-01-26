# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key, transport='rest')

img = PIL.Image.open("images/test_big_data.png")
#prompt = "Can you tell me about this photo?" + "please answer in traditional chinese"
#prompt = "請問這張照片的內容有什麼?"
prompt = "請問前三名跟佳作總共可獲得多少錢?"

model = genai.GenerativeModel("gemini-flash-latest")

result = model.generate_content( [prompt , img] )
print(result.text)
