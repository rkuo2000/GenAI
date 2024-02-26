## To run server: python whisper_server.py
## To run client: python post_audio.py

from flask import Flask, request, jsonify
import whisper
model = whisper.load_model("base")

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
        result = model.transcribe(audiofile.filename) 
        print(result["text"])
        return jsonify(result["text"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
