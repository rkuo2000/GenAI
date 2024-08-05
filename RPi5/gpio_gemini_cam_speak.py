#!/home/user/venv/bin/python

import os
from gtts import gTTS
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import cv2
from PIL import Image
import google.generativeai as genai

GOOGLE_API_KEY="get_api_key_from" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

sl = "zh-TW"
prompt = "Can you tell me about the scene? simple description in traditional chinese."

model = genai.GenerativeModel("gemini-1.5-flash")

# define Button pins
Button1 =  5
Button2 =  6
Button3 = 26

GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.system("mpg123 -q VLMStart_zhTW.mp3")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read() 
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(img)

    key1 = GPIO.input(Button1)
    key2 = GPIO.input(Button2)
    key3 = GPIO.input(Button3)
    print(key1, key2, key3)

    if key1==1:
       if key2==0:
           os.system("mpg123 -q ReportSensor_zhTW.mp3")
       if key3==0:
           #os.system("mpg123 -q SceneSnap_zhTW.mp3")
           result = model.generate_content( [prompt, image] )
           print(result.text)
           tts = gTTS(result.text, lang=sl )
           tts.save("gTTS.mp3")
           os.system("mpg123 -q gTTS.mp3")
           #cv2.imwrite("out.jpg", frame)
    else:
       if key2==0:
           os.system("mpg123 -q GeminiQA_zhTW.mp3")
       if key3==0:
           os.system("mpg123 -q VLMStart_zhTW.mp3")
    
