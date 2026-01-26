# pip install git+https://github.com/openai/whisper.git
# sudo apt install portaudio19-dev python3-pyaudio
# sudo apt install ffmpeg

import sys
inputfile = sys.argv[1]

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

import whisper
model = whisper.load_model("base").to(device)

result = model.transcribe(inputfile, fp16=False)
print(result["text"])
