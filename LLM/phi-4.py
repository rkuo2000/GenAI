# pip install transformers==4.53.3
# pip install trl==0.20.0
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "microsoft/Phi-4-mini-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

prompt = "Explain the concept of photosynthesis in a concise manner."

generated_text = generator(
    prompt,
    max_new_tokens=100,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)

print(generated_text[0]["generated_text"])

print("\n--- Another example: Coding help ---")
coding_prompt = "Write a Python function to calculate the factorial of a number."
generated_code = generator(
    coding_prompt,
    max_new_tokens=150,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)

print(generated_code[0]["generated_text"])
