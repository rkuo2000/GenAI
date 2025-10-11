### Spark-TTS
**Paper**: [Spark-TTS: An Efficient LLM-Based Text-to-Speech Model with Single-Stream Decoupled Speech Tokens](https://arxiv.org/abs/2503.01710)<br>
**Code**: [https://github.com/SparkAudio/Spark-TTS](https://github.com/SparkAudio/Spark-TTS)<br>

**Inference Overview of Voice Cloning** <br>
![](https://github.com/SparkAudio/Spark-TTS/raw/main/src/figures/infer_voice_cloning.png)
**Inference Overview of Controlled Generation** <br>
![](https://github.com/SparkAudio/Spark-TTS/raw/main/src/figures/infer_control.png)

**Kaggle**: [https://www.kaggle.com/code/rkuo2000/Spark-TTS](https://www.kaggle.com/code/rkuo2000/spark-tts)<br>

---
### IndexTTS2
**Paper**: [IndexTTS2: A Breakthrough in Emotionally Expressive and Duration-Controlled Auto-Regressive Zero-Shot Text-to-Speech](https://arxiv.org/abs/2506.21619)<br>
**Code**: [https://github.com/index-tts/index-tts](https://github.com/index-tts/index-tts)<br>
![](https://arxiv.org/html/2506.21619v2/x1.png)
![](https://arxiv.org/html/2506.21619v2/x2.png)

```
git lfs install
git clone https://github.com/index-tts/index-tts.git
cd index-tts
git lfs pull  # download large repository files
```
```
pip install -U uv
uv sync --all-extras
uv tool install "huggingface-hub[cli,hf_xet]"
hf download IndexTeam/IndexTTS-2 --local-dir=checkpoints

uv run tools/gpu_check.py
uv run webui.py
```

---
### FireRedTTS-2
**Paper**: [FireRedTTS-2: Towards Long Conversational Speech Generation for Podcast and Chatbot](https://arxiv.org/abs/2509.02020)<br>
**model**: [FireRedTeam/FireRedTTS2https](https://huggingface.co/FireRedTeam/FireRedTTS2)<br>
**Code**: [https://github.com/FireRedTeam/FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2)<br>
![](https://arxiv.org/html/2509.02020v2/image/tts_model_framework.png)
