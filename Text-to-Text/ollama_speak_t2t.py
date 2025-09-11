# pip install ollama
# pip install gtts
# pip install deep_translator
# usage: python ollama_speak.py "why is the sky blue" en

import sys
import os
import ollama
from gtts import gTTS
from deep_translator import GoogleTranslator

if len(sys.argv)>1:
    prompt = sys.argv[1]
    sl     = sys.argv[2]
else:
    prompt = "why is the sky blue?"
    sl     = "en"

stream = ollama.chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

text = ""
for chunk in stream:
   content = chunk['message']['content']
   if content!="." and content!="\n":
       text = text + content
   else:
       text = text + content
       print(text)
       # Translate to zh-TW
       tl = "zh-TW"   
       text = GoogleTranslator(source="auto", target=tl).translate(text=text) 
       # TTS
       tts = gTTS(text, lang=tl)
       tts.save("gTTS.mp3")
       os.system("mpg123 -q gTTS.mp3") 
       text = ""
