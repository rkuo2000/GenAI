from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

model_name = "mistralai/Mistral-7B-Instruct-v0.2"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
    {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
    {"role": "user", "content": "Do you have mayonnaise recipes?"}
]

inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")

generated_ids = model.generate(inputs_ids, max_new_tokens=1000, pad_token_id=2)
response = tokenizer.batch_decode(generated_ids)[0]
print(response)

