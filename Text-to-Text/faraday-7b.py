# pip install transformers accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "FelixChao/Faraday-7B"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language model."

input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")

output = model.generate(input_ids, max_length=128, num_beams=5, no_repeat_ngram_size=2)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)



