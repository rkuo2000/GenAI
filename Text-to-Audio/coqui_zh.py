# pip install TTS

import torch
from TTS.api import TTS

device = "cuda"

# TTS in Mandarin
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False).to(device)

text = "這是一個免費的文字轉語音的展示。"
outfile = "./output.wav"

tts.tts_to_file(text=text,file_path=outfile)

