# pip install transformers accelerate

import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="yentinglin/Taiwan-LLM-7B-v2.0.1-chat",torch_dtype=torch.bfloat16, device_map="auto")

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "你是一個人工智慧助理",
#       "content": "you are an assistant",
    },
    {"role": "user", "content": "東北季風如何影響台灣氣候？"},
#   {"role": "user", "content": "give me an introduction of Large Language Model"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print()
print(outputs[0]["generated_text"])

