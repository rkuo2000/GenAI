## To run server: python llm_server.py
## To run client: python post_text.py

# pip install flask requests jsonify 
# pip install accelerate

from flask import Flask, request, jsonify
import json

import transformers
from transformers import AutoModelForCausalLM , AutoTokenizer
import torch
torch.set_default_device("cuda")

model_name = "Q-bert/Mamba-130M"
#model_name = "Q-bert/Mamba-370M"
#model_name = "Q-bert/Mamba-790M"
#model_name = "Q-bert/Mamba-1B"
#model_name = "Q-bert/Mamba-3B"
#model_name = "Q-bert/Mamba-3B-slimpj"
#model_name = "ckip-joint/bloom-3b-zh"
#model_name = "Qwen/Qwen1.5-7B-Chat"
#model_name = "lmsys/vicuna-7b-v1.5-16k"
#model_name = "yentinglin/Taiwan-LLM-7B-v2.0.1-chat"
#model_name = "mistralai/Mistral-7B-Instruct-v0.2"
#model_name = "MediaTek-Research/Breeze-7B-Instruct-v0.1"

LLM = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto", device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hello"

@app.route("/text", methods=['POST'])
def text():
    if request.method == 'POST':
        prompt = request.json['text']
        print(prompt)

        input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
        output = LLM.generate(input_ids, max_length=64, num_beams=5, no_repeat_ngram_size=2)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("LLM: "+generated_text) 
        return jsonify(generated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
