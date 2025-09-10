# pip install google.generativeai

import google.generativeai as genai
import os

API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

## Setup Model
model_id = "gemini-2.5-flash"
print(model_id)

model = genai.GenerativeModel(model_id)

## Prompting
prompt = "What is LLM reasoning?"

## Generate content
response = model.generate_content([prompt])
print(response.text)

##------Streaming Output------------------------------------
#response = model.generate_content( [prompt], stream=True)
#for chunk in response:
#    print(chunk.text)
#    print("_" * 80)
