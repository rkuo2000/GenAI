from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
torch.set_default_device("cuda")

model_name = 'mtgv/MobileLLaMA-1.4B-Chat'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map='auto')

prompt = 'Q: What is the largest animal?\nA:'
input_ids = tokenizer.encode(prompt, return_tensors="pt")

generation_output = model.generate(input_ids=input_ids, max_new_tokens=64)
text_out = tokenizer.decode(generation_output[0])
print(text_out)
