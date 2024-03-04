from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype=torch.bfloat16, device_map="cuda", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

#prompt = "Give me a short introduction to large language model."
prompt = "Hello, How are you?"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = tokenizer([text], return_tensors="pt")
#inputs_ids = tokenizer.encode(prompt, return_tensors="pt")

outputs = model.generate(**inputs, max_length=64, pad_token_id=50256)
#outputs = model.generate(inputs_ids, max_length=512, pad_token_id=50256)

generated_text = tokenizer.decode(outputs[0])
print()
print(generated_text)
