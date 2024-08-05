### pip3 install gTTS
### Usage: python gTTS.py hello en

from gtts import gTTS
import sys
import os

text = sys.argv[1]
sl = sys.argv[2]

tts = gTTS(text,lang=sl)
tts.save('gTTS.mp3')

#os.system('mpg123 gTTS.mp3')  # Linux
#os.system('cmdmp3 gTTS.mp3') # Windows
