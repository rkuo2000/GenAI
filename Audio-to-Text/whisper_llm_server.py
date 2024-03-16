## To run server: python whisper_llm_server.py
## To run client: python post_audio.py (to post hello_howareyou.mp4)

from flask import Flask, request, jsonify
import torch

import whisper
WhisperModel = whisper.load_model("base")

import transformers
from transformers import AutoModelForCausalLM , AutoTokenizer

model_name = "Q-bert/Mamba-130M"
#model_name = "Q-bert/Mamba-370M"
#model_name = "Q-bert/Mamba-790M"
#model_name = "Q-bert/Mamba-1B"
#model_name = "Q-bert/Mamba-3B"
#model_name = "ckip-joint/bloom-3b-zh"

#LLM = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto", device_map="cuda")
LLM = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hello"

@app.route("/audio", methods=['POST'])
def audio():
    if request.method == 'POST':
        audiofile = request.files['audio'] 
        print(audiofile.filename)
        #audiofile.save(audiofile.filename)

        # transcribe
        result = WhisperModel.transcribe(audiofile.filename) 
        print("Whisper: "+result["text"])

        prompt = result["text"]
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
        output = LLM.generate(input_ids, max_length=64, num_beams=5, no_repeat_ngram_size=2)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("LLM: "+generated_text) 

        return jsonify(generated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
