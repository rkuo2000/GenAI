## To run server: python llava_server.py
## To run client: python post_imgtxt.py

# pip install fastapi uvicorn
# pip install accelerate

from PIL import Image
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response
import requests
import uvicorn

from pydantic import BaseModel


from transformers import AutoProcessor, AutoModelForCausalLM
import torch

model_id = "microsoft/Phi-3-vision-128k-instruct" 

model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda", trust_remote_code=True, torch_dtype="auto")

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) 

generation_args = { 
    "max_new_tokens": 500, 
    "temperature": 0.0, 
    "do_sample": False, 
} 

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def home():
    return Response("Hello World")

@app.post("/imgtxt")
def post_imgtxt(image: UploadFile = File(...), text: str = Form(...)):
    print(image.filename)
    print(text)
    with open(image.filename, "wb") as f:
        content = image.file.read()
        f.write(content)
    f.close()

    # LLaVA
    print(image.filename)
    img = Image.open(image.filename)
    inst = ", please answer in a simple sentence"
    messages = [
        {"role": "user", "content": "<|image_1|>\n"+text+inst}, # "What is shown in this image?"}, 
    ]    
    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(prompt, [img], return_tensors="pt").to("cuda:0") 
    generate_ids = model.generate(**inputs, eos_token_id=processor.tokenizer.eos_token_id, **generation_args) #max_new_tokens=200
    
    # remove input tokens 
    outputs = generate_ids[:, inputs['input_ids'].shape[1]:]
    result = processor.batch_decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] 
    print(result)
    return Response(result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
