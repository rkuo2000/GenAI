import sys
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

model_id = 'openbmb/MiniCPM-Llama3-V-2_5-int4'
model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

#filepath = "images/NTOU_frontgate.jpg"
filepath = sys.argv[1]
image = Image.open(filepath)
#image.show()

#question = 'What is in the image?'
question = '這是基隆的那個著名景點?'
msgs = [{'role': 'user', 'content': question}]

res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=tokenizer,
    sampling=True, # if sampling=False, beam_search will be used by default
    temperature=0.7,
    # system_prompt='' # pass system_prompt if needed
)
print(res)
