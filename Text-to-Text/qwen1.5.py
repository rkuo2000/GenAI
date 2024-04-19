# pip install transformers accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

model_name = "Qwen/Qwen1.5-7B-Chat"
print(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print()

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]

inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)

generated_ids = model.generate(inputs_ids, max_new_tokens=256, pad_token_id=tokenizer.eos_token_id)

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
