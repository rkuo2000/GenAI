# pip install tranformers
# pip install -qU huggingface_hub

import os
ACCESS_TOKEN=os.environ.get("HF_ACCESS_TOKEN")

from huggingface_hub import login
login(token=ACCESS_TOKEN)

from transformers import AutoTokenizer, Gemma3ForConditionalGeneration
from PIL import Image
import requests
import torch

model_id = "taide/Gemma-3-TAIDE-12b-Chat"
model = Gemma3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

tokenizer = AutoTokenizer.from_pretrained(model_id)

sys = "你是一個優秀的軟硬體設計工程師"
question = "設計一個用微控制器製作的邊緣智慧裝置,請詳細介紹其應有的先進功能,並仔細介紹設計製作的細節?"

#chat = [ {"role": "user", "content": f"{question}"}, ]
chat = [
    { "role": "system", "content": f"{sys}" },
    { "role": "user",   "content": f"{question}" },
]

prompt = tokenizer.apply_chat_template(chat, add_generation_prompt=True, tokenize=True)

## Apply template & Generate output
generated = model.generate(prompt, max_new_tokens=100, do_sample=False)

## Decode output & Print
decoded = tokenizer.decode(generated,skip_special_tokens=True)[0]
print(decoded)
