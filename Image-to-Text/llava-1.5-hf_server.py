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

# Llava 1.5 is using LlavaForConditionGeneration
from transformers import AutoProcessor, LlavaForConditionalGeneration
from transformers import BitsAndBytesConfig
import torch

model_name = "llava-hf/llava-1.5-7b-hf"

quantization_config = BitsAndBytesConfig( load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16 )

model = LlavaForConditionalGeneration.from_pretrained(model_name, quantization_config=quantization_config, device_map="auto")
processor = AutoProcessor.from_pretrained(model_name)


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
    inputs = processor(text=text, images=img, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=200)
    generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
    result = generated_text.split("ASSISTANT:")[-1]
    print(result)
    return Response(result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
