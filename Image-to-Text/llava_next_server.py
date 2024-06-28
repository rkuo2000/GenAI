## To run client: python post_imgtxt.py

# pip install fastapi uvicorn
# pip install accelerate

from PIL import Image
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response
import requests
import uvicorn

from pydantic import BaseModel

from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch

model_id = "llava-hf/llava-v1.6-vicuna-7b-hf"

processor = LlavaNextProcessor.from_pretrained(model_id)

model = LlavaNextForConditionalGeneration.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True, load_in_4bit=True)


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

    # VLM = LlavaNext
    print(image.filename)
    img = Image.open(image.filename)
    prompt = "USER: <image>\n"+text+"\nASSISTANT:"    
    inputs = processor(text=prompt, images=img, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=200)
    generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
    result = generated_text.split("ASSISTANT:")[-1]
    print(result)
    return Response(result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
