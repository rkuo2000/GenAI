# pip install transformers accelerate 
# pip insdtall sentencepiece

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

model_name = "lmsys/vicuna-7b-v1.5-16k"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print()

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")

generated_ids = model.generate(input_ids, max_new_tokens=128)
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
