# pip install git+https://github.com/openai/whisper.git

import whisper
model = whisper.load_model("base")

inputfile = "audio0.aac"
#inputfile = "audio1.flac"
#inputfile = "audio2.mp3"
#inputfile = "audio3.mp4"

result = model.transcribe(inputfile)

print(result["text"])
