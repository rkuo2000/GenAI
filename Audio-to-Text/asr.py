# pip install git+https://github.com/openai/whisper.git

import whisper
ASR = whisper.load_model("base")

#inputfile = "audio0.aac"
#inputfile = "audio1.flac"
#inputfile = "audio2.mp3"
#inputfile = "audio3.mp4"
inputfile = "gTTS.mp3"

result = ASR.transcribe(inputfile)

print(result["text"])
