#!/home/user/venv/bin/python
## pip install ultralytics
## pip install deep-translator
## pip install gtts

import os
import cv2
from ultralytics import YOLO
from deep_translator import GoogleTranslator
from gtts import gTTS

model = YOLO("yolov10n.pt")

def Speak(text,tl):
    # Translate
    text = GoogleTranslator(source="auto", target=tl).translate(text=text)
    print(text)
    ## TTS
    tts = gTTS(text, lang=tl)
    tts.save("gTTS.mp3")
    ## Speak
    os.system("mpg123 -q gTTS.mp3")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 1) # mirror

    ## Object Detection 
    results = model(frame)

    ## Object Counting
    labels = results[0].names
    cls = results[0].boxes.cls.tolist()
    unique = list(dict.fromkeys(cls))

    sl = "en"
    text = "There are "
    for label in unique:
        count = cls.count(label)
        text = text + str(count) + " " + labels[int(label)] + ","
    #print(text)
    Speak(text, "zh-TW")

    #results[0].save("out.jpg")
    #img = cv2.imread("out.jpg")
    #cv2.imshow('webcam', img)

    #k = cv2.waitKey(1) & 0xFF
    #if k==ord('s'):
    #    cv2.imwrite("detected.jpg", img)
    #    #Speak(text,sl)
    #    Speak(text, "zh-TW")
    #if k==27:
    #    break

cap.release()
cv2.destroyAllWindows()
