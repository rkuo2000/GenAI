# pip install git+https://github.com/huggingface/transformers.git
# pip install accelerate

import torch
from transformers import pipeline

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
print(model_name)

pipe = pipeline("text-generation", model=model_name, torch_dtype=torch.bfloat16, device_map="auto")

prompt = "How many helicopters can a human eat in one sitting?"
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": prompt},
]

inputs = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(inputs, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)[0]
textout = outputs["generated_text"].split("<|assistant|>")[-1]
print(textout)
