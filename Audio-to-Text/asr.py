# pip install git+https://github.com/openai/whisper.git
# pip install pyaudio
# Download ffmpeg.exe

import whisper
ASR = whisper.load_model("base").to("cpu")

#inputfile = "audio0.aac"
#inputfile = "audio1.flac"
#inputfile = "audio2.mp3"
#inputfile = "audio3.mp4"
inputfile = "gTTS.mp3"

result = ASR.transcribe(inputfile, fp16=False)

print(result["text"])
