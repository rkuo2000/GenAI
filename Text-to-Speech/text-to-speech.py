# pip install text-to-speech

import text_to_speech as tts

#lang = "en" # IETF lanuage tag
lang = "zh" # IETF lanuage tag

#text = "Text-to-Speech is great and useful tool"
text = "請列出五種知名的台灣美食"

tts.save(text, lang, file="tts.mp3")
