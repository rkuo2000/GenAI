## To run server: python llm_server.py
## To run client: python post_text.py

# pip install fastapi uvicorn
# pip install accelerate

from fastapi import FastAPI, Request
from fastapi.responses import Response
import uvicorn

from pydantic import BaseModel

import torch
import transformers
from transformers import AutoModelForCausalLM , AutoTokenizer

### https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
#model_name = "Q-bert/Mamba-130M"
#model_name = "Q-bert/Mamba-370M"
#model_name = "Q-bert/Mamba-790M"
#model_name = "Q-bert/Mamba-1B"
#model_name = "Q-bert/Mamba-3B"
#model_name = "Q-bert/Mamba-3B-slimpj"
#model_name = "ckip-joint/bloom-3b-zh" # zh
#model_name = "google/gemma-2b-it"
#model_name = "microsoft/phi-2"
#model_name = "mistralai/Mistral-7B-Instruct-v0.2"
#model_name = "meta-llama/Llama-2-7b-chat-hf"

#model_name = "Qwen/Qwen1.5-7B-Chat" # cn
#model_name = "lmsys/vicuna-7b-v1.5-16k" # cn/zh
#model_name = "yentinglin/Taiwan-LLM-7B-v2.0.1-chat" # zh
#model_name = "MediaTek-Research/Breeze-7B-Instruct-v0.1" # zh/cn
model_name = "INX-TEXT/Bailong-instruct-7B" # zh

print(model_name)

#LLM = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto", device_map="cuda")
LLM = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="cuda")

tokenizer = AutoTokenizer.from_pretrained(model_name)

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

    input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    output = LLM.generate(input_ids, max_length=128, num_beams=5, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("LLM: "+generated_text) 
    return Response(generated_text)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
