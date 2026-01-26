# Transcribe gTTS.mp3 to text

import whisper
ASR = whisper.load_model("base")

result = ASR.transcribe("gTTS.mp3")
print(result["text"])
