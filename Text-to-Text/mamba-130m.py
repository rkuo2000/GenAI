# pip install tranformers einops

import transformers
transformers.logging.set_verbosity_error()

from transformers import AutoModelForCausalLM , AutoTokenizer

model = AutoModelForCausalLM.from_pretrained('Q-bert/Mamba-130M', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('Q-bert/Mamba-130M')

prompt = "Hi, how are you ?"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

output = model.generate(input_ids, max_length=64, num_beams=5, no_repeat_ngram_size=2)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)

