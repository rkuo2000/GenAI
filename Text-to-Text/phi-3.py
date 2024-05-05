from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

#model_name = "microsoft/Phi-3-mini-4k-instruct" # 3.8B
model_name = "microsoft/Phi-3-mini-128k-instruct" # 3.8B
print(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

prompt = '''
def print_prime(n):
    """
    Print all primes between 1 and n
    """
'''

inputs = tokenizer(prompt, return_tensors="pt")

generated_ids = model.generate(**inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)
response = tokenizer.batch_decode(generated_ids)[0]
print(response)

