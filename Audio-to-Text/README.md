# Audio-To-Text sample codes

---
## ASR (Automatic Speech Recognition)
`pip install git+https://github.com/openai/whisper.git`<br>
`pip install gTTS`<br>

To generate gTTS.mp3: `python ../gTTS.py "早安你好"`<br>

### OpenAI/Whisper
`python asr.py`<br>

### Faster-Whisper
`python faster_asr.py`<br>

### Nvidia Canary
`pyton canary-1b.py`<br>

---
### Whisper Servers

* run Whisper Server on PC: `python whisper_server.py`<br>

* run Whisper+LLM Server on PC+GPU: `python whisper_llm_server.py`<br>

* run Client on PC to test Server: `python post_audio.py`<br>
