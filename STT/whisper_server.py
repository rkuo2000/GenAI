# pip install git+https://github.com/openai/whisper.git
## To run server: python whisper_server.py
## To run client: python post_audio.py

# pip install git+https://github.com/openai/whisper.git
# pip install fastapi uvicorn
# pip install nest-asyncio

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from pydantic import BaseModel
import uvicorn
import json

import whisper
ASR = whisper.load_model("base").to("cpu")

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def home():
    return Response("Hello World!")

@app.route("/", methods=['GET'])
def hello():
    return "hello"

@app.post("/audio")
def post_audio(audio: UploadFile = File(...)):
    print(audio.filename)
    fname = 'tmp_'+audio.filename
    with open(fname, 'wb') as f:
        content = audio.file.read()
        f.write(content)

    # Whisper transcribe
    result = ASR.transcribe(fname,fp16=False)
    print("ASR: "+result["text"])
    return Response(result["text"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")


