# pip install tranformers einops

import transformers

from transformers import AutoModelForCausalLM , AutoTokenizer, BitsAndBytesConfig
import torch

#model_name = "google/gemma-1.1-2b-it"
model_name = "google/gemma-1.1-7b-it"
print(model_name)

quantization_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=quantization_config, device_map="auto")

#model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")

tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Write me a poem about Machine Learning."
input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

output = model.generate(**input_ids, max_new_tokens=128, pad_token_id=tokenizer.eos_token_id)
generated_text = tokenizer.decode(output[0])
print(generated_text)
