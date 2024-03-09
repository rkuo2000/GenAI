import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.set_default_device("cuda")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

prompt = '''
def print_prime(n):
    """
    Print all primes between 1 and n
    """
'''

inputs = tokenizer(prompt, return_tensors="pt")

generated_ids = model.generate(**inputs, max_length=200, pad_token_id=50256)
response = tokenizer.batch_decode(generated_ids)[0]
print(response)

