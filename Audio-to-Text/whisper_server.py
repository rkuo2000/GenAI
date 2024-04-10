# pip install git+https://github.com/openai/whisper.git
## To run server: python whisper_server.py
## To run client: python post_audio.py

from flask import Flask, request, jsonify
import whisper
ASR = whisper.load_model("base")

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
        result = ASR.transcribe(audiofile.filename) 
        print(result["text"])
        return jsonify(result["text"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
