# pip install ollama
# pip install gtts
# pip install mpg123
# usage: python ollama_speak.py "why is the sky blue" en

import sys
import ollama
from gtts import gTTS
from mpg123 import Mpg123, Out123

if len(sys.argv)>1: 
    prompt = sys.argv[1]
    sl     = sys.argv[2]
else:
    prompt = "why is the sky blue?"
    sl     = "en"
    #prompt = "請列出五項台灣著名的美食"
    #sl = "zh-TW"

stream = ollama.chat(
#    model='llama3.1',
#    model='tinyllama',
    model='snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0', # TAIDE
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
       mp3 = Mpg123("gTTS.mp3")
       out = Out123()
       for frame in mp3.iter_frames(out.start):
           out.play(frame)
       text = ""
