#!/home/user/venv/bin/python

import os

import cv2
from PIL import Image
import google.generativeai as genai

GOOGLE_API_KEY="get_api_key_from" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

sl = "zh-TW"
prompt = "Can you tell me about the scene? simple description in traditional chinese."

model = genai.GenerativeModel("gemini-2.5-flash")

while True:

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read() 
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = model.generate_content( [prompt, image] )
    print(result.text)
    
