# sudo apt install mpg123
# pip install ollama
# pip install gtts

import ollama
from gtts import gTTS
import os

sl = "en"

stream = ollama.chat(
    model='tinyllama',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

text = ""
for chunk in stream:
   content = chunk['message']['content']
   if content!=".":
       text = text + " " + content
   else:
       print(text)
       tts = gTTS(text, lang=sl)
       tts.save("gTTS.mp3")
       os.system("mpg123 -q gTTS.mp3")
       text = ""
