# pip install TTS

import torch
from TTS.api import TTS

device = "cuda"

# TTS in English
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)

text = "Text to speech is a great and useful tool"
outfile = "./output.wav"

tts.tts_to_file(text=text, file_path=outfile)
