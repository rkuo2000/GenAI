# Generative AI sample codes

## Audio-to-Text
* `post_audio.py` : HTTP Post audio file to a http-server
* `whisper_server.py` : HTTP server to receive audio file and transcribe to text
* `whisper_llm_server.py` : HTTP server to transcribe audio file to text, and text-to-text by calling a LLM model

---
## Text-to-Text (LLMs)
* `post_text.py` for HTTP POST text to the LLM Server
* `llm_server.py` for runing a LLM Server
* `bloom-zh.py`
* `breeze-7b-instruct.py`
* `faraday-7b.py`
* `mamba-130m.py` # also for -370M, -790M, -1B, -3B, -3B-slimpj
* `mistral-7b-instruct.py`
* `phi-2.py`
* `qwen1.5-7b-chat.py`
* `taiwan-llm.py`
* `vicuna-7b-v1.5.py`
### post_text from PC to a LLM_Server
![](https://github.com/rkuo2000/GenAI/blob/main/assets/pyngrok_post_text.png?raw=true)
### pyngrok_LLM_Server (on Colab T4)
![](https://github.com/rkuo2000/GenAI/blob/main/assets/pyngrok_LLM_Server.png?raw=true)

---
## Text-to-Speech

* **Bark TTA**: `python bark_en.py`, `python bark_cn.py`
* **coqui TTS**: `python coqui_en.py`, `python coqui_zh.py`
* **text-to-speech**: `python text_to_speech.py`
* **gTTS**: `python gTTS.py "你好?" zh`
* **gTranslate**: `python gTranslate.py`
* 
---
## Image-to-Text
* **LLaVA**
* `llava-1.5-7b.py` - test LLaVA model
* `post_imgtxt.py`  - http post the image + text to LLaVA server


---
## Text-to-Image 
* `sdxl-base.py` - run SDXL-base model to input text and generate an image
* `sdxl-lightning-lora.py` - run SDXL-Lightning with LoRA model to use text to generate an image
* `sdxl-lightning-unet.py` - run SDXL-Lightning with UNet model to use text to generate an image

---
## Image-to-3D

### TripoSR

* Installation :
```
git clone https://github.com/VAST-AI-Research/TripoSR`
cd TripoSR
pip install -r rewquirements.txt
pip install -e .
```
* To run a test
`python run.py examples/chair.png`<br>
(output/0/mesh.obj can be viewed by using F3D viewer, Blender (Game Engine), or Cura(3D-print Slicer)<br>

* To run a Gradio server 
`python gradio_app.py` : running GUI server<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/TripoSR_gradio_server.png?raw=true)

### Text-to-3D
**gTranslate + SDXL-Lightning + TripoSR + AppInventor2**<br>

To modify `gradio_app.py` to add *sdxl-lightning-lora.py* funciton




