# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxx" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

## Setup Model
model_id = "gemini-2.0-flash"

model = genai.GenerativeModel(model_id)

## Prompting
prompt = "What is large language model?"

## Generate content
response = model.generate_content( [prompt] )

print(response.text)

##------Streaming Output------------------------------------
#response = model.generate_content( [prompt], stream=True)
#for chunk in response:
#    print(chunk.text)
#    print("_" * 80)
