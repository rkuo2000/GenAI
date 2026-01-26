# pip install git+https://github.com/huggingface/parler-tts.git

from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"

model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler_tts_mini_v0.1").to(device)
tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler_tts_mini_v0.1")

prompt = "Hey, how are you doing today?"
description = "A female speaker with a slightly low-pitched voice delivers her words quite expressively, in a very confined sounding environment with clear audio quality. She speaks very fast."

input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

generation = model.generate(input_ids=input_ids, max_new_tokens=4096, prompt_input_ids=prompt_input_ids)
audio_arr = generation.cpu().numpy().squeeze()
#sf.write("parler_tts_out.wav", audio_arr, model.config.sampling_rate)
sf.write("parler_tts_out.mp3", audio_arr, model.config.sampling_rate)
