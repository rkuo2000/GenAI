# pip install ollama
# pip install gtts
# usage: python ollama_speak.py "why is the sky blue" en

import sys
import os
import ollama
from gtts import gTTS

if len(sys.argv)>1: 
    prompt = sys.argv[1]
    sl     = sys.argv[2]
else:
    #prompt = "why is the sky blue?"
    #sl     = "en"
    prompt = "請列出五項台灣著名的美食"
    sl = "zh-TW"

stream = ollama.chat(
#    model='snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0', # TAIDE
#    model='llama3.1',
#    model='tinyllama',
    model='gemma2:2b',
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
       tts = gTTS(text, lang=sl)
       tts.save("gTTS.mp3")
       os.system("mpg123 -q gTTS.mp3")
       text = ""
