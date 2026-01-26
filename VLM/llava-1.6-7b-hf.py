from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
import sys
from PIL import Image
import requests

model_id = "llava-hf/llava-v1.6-vicuna-7b-hf"

processor = LlavaNextProcessor.from_pretrained(model_id)

model = LlavaNextForConditionalGeneration.from_pretrained( model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True, load_in_4bit=True)

#url = "https://github.com/haotian-liu/LLaVA/blob/1a91fc274d7c35a9b50b3cb29c4247ae5837ce39/images/llava_v1_5_radar.jpg?raw=true"
#image = Image.open(requests.get(url, stream=True).raw)

filepath = sys.argv[1]
image = Image.open(filepath)
prompt = "USER: <image>\nWhat is in this image? ASSISTANT:"

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

# autoregressively complete prompt
output = model.generate(**inputs, max_new_tokens=100)

print(processor.decode(output[0], skip_special_tokens=True))

