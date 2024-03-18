# Transcribe gTTS.mp3 to text

import whisper
model = whisper.load_model("base")

result = model.transcribe("gTTS.mp3")
print(result["text"])
