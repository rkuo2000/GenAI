# usage: python gT2T.py "How are you" fr

import sys
from deep_translator import GoogleTranslator

if len(sys.argv)>1:
    text = sys.argv[1]
    tl   = sys.argv[2]
else:
    text = "how are you"
    tl   = "zh-TW"

outtext = GoogleTranslator(source="auto", target=tl).translate(text=text)

print(outtext)
