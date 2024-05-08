## To run server: python llama_cpp_server.py
## To run client: python llm_client.py
## To run client: python post_text.py

# pip install llama-cpp-python
# pip install fastapi uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import Response
import uvicorn

from pydantic import BaseModel

import torch
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_name = "taide/Llama3-TAIDE-LX-8B-Chat-Alpha1-4bit" # TAIDE
model_file = "taide-8b-a.3-q4_k_m.gguf"

model_path = hf_hub_download(model_name, filename=model_file)
print(model_file)

LLM = Llama(model_path=model_path, n_ctx=16000, n_threads=32, n_gpu_layers=0)

app = FastAPI()

class UserData(BaseModel):
    text: str

@app.get("/")
def root():
    return Response("Hello World!")

@app.post("/text")
def text(user_data: UserData):
    prompt = user_data.text
    print(prompt)

    outputs = LLM(prompt, max_tokens=32, stop=["Q:", "\n"], echo=False)
    out_text = outputs["choices"][0]["text"]
    print("LLM: "+out_text) 
    return Response(out_text)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
