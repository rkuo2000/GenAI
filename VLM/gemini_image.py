# pip install google-genai

from google import genai
import PIL.Image
import os
import sys

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv)>1:
    filename = sys.argv[1]
else:
    filename = "images/test_big_data.png"

img = PIL.Image.open(filename)

#prompt = "Can you tell me about this photo?" + "please answer in traditional chinese"
prompt = "請問前三名跟佳作總共可獲得多少錢?"

reponse = client.models.generate_content(
    model ="gemini-3-flash-preview",
    contents = [prompt , img]
)
print(response.text)
