# pip install tranformers

from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import GenerationConfig
from transformers import pipeline
import torch
torch.set_default_device("cuda")

model_name = "ckip-joint/bloom-3b-zh"

model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, low_cpu_mem_usage=True, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, use_fast=False)

#prompt = "Hi, how are you ?"
prompt = "所以你會講中文?"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

output = model.generate(input_ids, max_length=64, num_beams=5, no_repeat_ngram_size=2)
result = tokenizer.decode(output[0])
print(result)
