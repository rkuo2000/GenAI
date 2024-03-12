# !pip install --upgrade -q accelerate bitsandbytes
# !pip install git+https://github.com/huggingface/transformers.git

from transformers import pipeline
from transformers import BitsAndBytesConfig
import torch
import requests
from PIL import Image

model_id = "llava-hf/llava-1.5-7b-hf"

quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)

pipe = pipeline("image-to-text", model=model_id, model_kwargs={"quantization_config": quantization_config})

#image1 = Image.open(requests.get("https://llava-vl.github.io/static/images/view.jpg", stream=True).raw)
#image1 = Image.open("images/Tsai_IngWen.jpg")
image1 = Image.open("images/Taiwan_weather-2024-03-12-13-00.jpg")

#prompt = "USER: <image>\nWhat are the things I should be cautious about when I visit this place?\nASSISTANT:"
#prompt = "USER: <image>\n請問這個地方適合全家遊玩嗎?\nASSISTANT:"
#prompt = "USER: <image>\nDo you know who that is?\nASSISTANT:"
prompt = "USER: <image>\n根據這張的氣象衛星雲圖,請詳細說明台灣地區的今天的天氣跟未來的天氣如何?\nASSISTANT:"

max_new_tokens = 1000
outputs = pipe(image1, prompt=prompt, generate_kwargs={"max_new_tokens": max_new_tokens})

print(outputs[0]["generated_text"])
