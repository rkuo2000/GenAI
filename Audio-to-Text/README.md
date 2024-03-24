# Audio-To-Text sample codes
* `python ../gTTS.py "how are you today" en` : to generate gTTS.mp3
* `post_audio.py` : HTTP Post audio file to a http-server
* `whisper_server.py` : HTTP server to receive audio file and transcribe to text
* `whisper_llm_server.py` : HTTP server to transcribe audio file to text, and text-to-text by calling a LLM model
  
## Installation
`pip install requests flask`<br>
`pip install git+https://github.com/openai/whisper.git`<br>
`pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git` (whisper large v2)

---
## ASR (Automatic Speech Recognition)

### OpenAI/Whisper
`python asr.py`<br>

### Faster-Whisper
`python faster_asr.py`<br>

### Nvidia Canary
`python ../gTTS.py "comment allez-vous aujourd'hui" fr`<br>
`pyton canary-1b.py`<br>

---
### HTTP Servers

* To test **Whisper** server:
`python whisper_server.py` - running Whisper http-server<br>
`python post_audio.py` - running http-post audio file to server<br>

* To test **Whisper+LLM** server:
`python whisper_llm_server.py` - running Whiserp+LLM http-server<br>
`python post_audio.py` - running http-post audio file to server<br>

