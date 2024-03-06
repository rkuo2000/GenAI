# pip install text-to-speech

from text_to_speech import save

language = "en" # IETF lanuage tag

text = "Text-to-Speech is great and useful tool"
outfile = "output.mp3"

save(text, language, file=outfile)
