## To run client: python post_imgau.py

# pip install fastapi uvicorn
# pip install accelerate

from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import requests
import uvicorn

from pydantic import BaseModel

from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch

model_id = "llava-hf/llava-v1.6-vicuna-7b-hf"

processor = LlavaNextProcessor.from_pretrained(model_id)

model = LlavaNextForConditionalGeneration.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True, load_in_4bit=True)


import whisper
WhisperModel = whisper.load_model("base")

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def home():
    return Response("Hello World")

@app.post("/multi")
async def post_multi(image: UploadFile, audio: UploadFile ):
    print(audio.filename)
    with open(audio.filename, "wb") as f:
        content = audio.file.read()
        f.write(content)
    f.close()
    print(image.filename)
    with open(image.filename, "wb") as f:
        content = image.file.read()
        f.write(content)
    f.close()

    # Whisper (ASR)
    result = WhisperModel.transcribe(audio.filename)
    #print("Whisper: "+result["text"])

    # LLaVA (VLM)
    text = result["text"]
    print(text)
    img = Image.open(image.filename)
    prompt = "USER: <image>\n"+text+"\nASSISTANT:"
    inputs = processor(prompt, img, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=100)
    generated_text = processor.decode(output[0], skip_special_tokens=True)
    #result = generated_text.split("ASSISTANT:")[-1]
    print(generated_text)
    return Response(generated_text)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
