#!/home/user/venv/bin/python

import os
import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# define Button pins
Button1 =  5
Button2 =  6
Button3 = 26

GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    key1 = GPIO.input(Button1)
    key2 = GPIO.input(Button2)
    key3 = GPIO.input(Button3)
    print(key1, key2, key3)

    if key1==1:
       if key2==0:
           os.system("mpg123 -q ReportSensor_zhTW.mp3")
       if key3==0:
           os.system("mpg123 -q SceneSnap_zhTW.mp3")
    else:
       if key2==0:
           os.system("mpg123 -q GeminiQA_zhTW.mp3")
       if key3==0:
           os.system("mpg123 -q VLMStart_zhTW.mp3")
    
    sleep(1)
