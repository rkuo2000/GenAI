import sys
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

model_id = 'openbmb/MiniCPM-Llama3-V-2_5-int4'
model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

imgfile = "images/NTOU_frontgate.jpg"
image = Image.open(imgfile)
#image.show()

question = 'What is in the image?'
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
