# !pip install --upgrade -q accelerate bitsandbytes
# !pip install git+https://github.com/huggingface/transformers.git

## To run server: python3 llava_server.py
## To run client: python3 post_imgtxt.py

import base64
import time
from flask import Flask, request, jsonify
from transformers import pipeline
from transformers import BitsAndBytesConfig
import torch

model_id = "llava-hf/llava-1.5-7b-hf"
quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
pipe = pipeline("image-to-text", model=model_id, model_kwargs={"quantization_config": quantization_config})


app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "hello"

@app.route("/imgtxt", methods=['POST'])
def imgtxt():
    if request.method == 'POST':
        # Access the raw input stream of the request
        stream = request.stream
        
        # Read the stream in chunks
        CHUNK_SIZE = 1024  # Adjust chunk size as needed
        data = b''
        while True:
            chunk = stream.read(CHUNK_SIZE)
            if not chunk:
                break
            data += chunk
        
        # Print the binary stream
        # print("Received POST request data:", data)
        
        decoded_data = base64.b64decode(data)
        max_new_tokens = 200
        outputs = pipe(image1, prompt=prompt, generate_kwargs={"max_new_tokens": max_new_tokens})
        print(outputs[0]["generated_text"])
        return jsonify(outputs[0]["generated_text"])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
