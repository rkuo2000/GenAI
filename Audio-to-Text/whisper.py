# pip install git+https://github.com/openai/whisper.git
# pip install pyaudio
# Download ffmpeg.exe

import whisper
#model = whisper.load_model("base").to("cpu")
model = whisper.load_model("base")

#inputfile = "audio/audio1.flac"
#inputfile = "audio/audio2.mp3"
#inputfile = "audio/audio3.mp4"
inputfile = "gTTS.mp3"

result = model.transcribe(inputfile, fp16=False)

print(result["text"])
