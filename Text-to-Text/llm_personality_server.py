## To run server: python llm_personality_server.py
## To run client: python llm_client.py

# pip install fastapi uvicorn
# pip install accelerate

from fastapi import FastAPI, Request
from fastapi.responses import Response
import uvicorn

from pydantic import BaseModel

import torch
import transformers
from transformers import AutoModelForCausalLM , AutoTokenizer

#model_name="MediaTek-Research/Breeze-7B-Instruct-v0.1"
model_name="meta-llama/Llama-2-7b-chat-hf"

print(model_name)

LLM = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="cuda")

tokenizer = AutoTokenizer.from_pretrained(model_name)

Role = "you are a human companion"


app = FastAPI()

class UserData(BaseModel):
    text: str

@app.get("/")
def root():
    return Response("Hello World!")

@app.post("/text/")
def text(user_data: UserData):
    prompt = user_data.text
    print(prompt)

    messages = [{"role": "system", "content": Role}]
    messages.append({"role": "user", "content": prompt})
    print(messages)

    input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
    generated_ids = LLM.generate(input_ids, max_new_tokens=256)
    output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    textout = output.split("[/INST]")[-1]
    print("LLM: "+textout) 
    return Response(textout)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
