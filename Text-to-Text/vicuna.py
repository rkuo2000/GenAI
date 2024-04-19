# pip install transformers accelerate 
# pip insdtall sentencepiece

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "lmsys/vicuna-7b-v1.5"
print(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print()

prompt = "Give me a short introduction to large language model."

input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

generated_ids = model.generate(**input_ids, max_new_tokens=128, do_sample=True)

output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(output)
