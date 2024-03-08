## To run server: python whisper_server_llm.py
## To run client: python post_audio.py (to post hello_howareyou.mp4)

from flask import Flask, request, jsonify
import whisper

WhisperModel = whisper.load_model("base")

import transformers
from transformers import AutoModelForCausalLM , AutoTokenizer

MambaLLM = AutoModelForCausalLM.from_pretrained('Q-bert/Mamba-130M', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('Q-bert/Mamba-130M')

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "hello"

@app.route("/audio", methods=['POST'])
def audio():
    if request.method == 'POST':
        audiofile = request.files['audio'] 
        print(audiofile.filename)
        #audiofile.save(audiofile.filename)
        audiofile.save("tmp_"+audiofile.filename)

        # transcribe
        result = WhisperModel.transcribe(audiofile.filename) 
        print("Whisper: "+result["text"])

        prompt = result["text"]
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = MambaLLM.generate(input_ids, max_length=64, num_beams=5, no_repeat_ngram_size=2)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("Mamba: "+generated_text) 

        return jsonify(generated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
