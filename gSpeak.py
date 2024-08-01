## pip install gtts
## pip install deep-translator
# usage: python gT2T.py "How are you" fr

import sys
import os
from gtts import gTTS
from deep_translator import GoogleTranslator

if len(sys.argv)>1:
    text = sys.argv[1]
    tl   = sys.argv[2]
else:
    text = "how are you"
    tl   = "zh-TW"

outtext = GoogleTranslator(source="auto", target=tl).translate(text=text)
print(outtext)

tts = gTTS(outtext,lang=tl)
tts.save('gTTS.mp3')

os.system('mpg123 -q gTTS.mp3')  # Linux
#os.system('cmdmp3 gTTS.mp3') # Windows

