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
### Whisper Server
Use one of the following:

1. run Whisper Server on PC: `python whisper_server.py`<br>

2. run Whisper+LLM Server on PC+GPU: `python whisper_llm_server.py`<br>

3. run Whisper+LLM Server on Colab T4: use Colab.research.google.com to open `pyngrok_Whisper_LLM_Server.ipynb`<br>

### Whisper Client

* run Client on PC to test Server: `python post_audio.py`<br>

---
### [Omnilingual](https://github.com/facebookresearch/omnilingual-asr)
`pip install omnilingual-asr`<br>

```
from omnilingual_asr.models.inference.pipeline import ASRInferencePipeline

pipeline = ASRInferencePipeline(model_card="omniASR_LLM_Unlimited_7B_v2")
audio_files = ["/path/to/eng_audio1.flac", "/path/to/deu_audio2.wav"]
lang = ["eng_Latn", "deu_Latn"]
transcriptions = pipeline.transcribe(audio_files, lang=lang, batch_size=2)
```

