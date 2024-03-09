# Generative AI sample codes

## Audio-to-Text
* `post_audio.py` : HTTP Post audio file to a http-server
* `whisper_server.py` : HTTP server to receive audio file and transcribe to text
* `whisper_llm_server.py` : HTTP server to transcribe audio file to text, and text-to-text by calling a LLM model

---
## Text-to-Speech

### Bark TTA
`bark_en.py` (English)<br> 
`bark_cn.py` (Simplified Chinese)<br>
`bark_zh.py` (Traditional Chinese)<br>

### Coqui TTS
`coqui_en.py` (English)<br>
`coqui_zh.py` (Traditional Chinese)<br>

### text-to-speech 
`text_to_speech.py` (English)<br>

---
## Image-to-Text
* `llava-1.5-7b.py` - test LLaVA model
* `llava_server.py` - run a LLaVA http server
* `post_imgtxt.py`  - http post the image + text to http server (LLaVA server)

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

### Text-to-3D ( = Text-to-Image + Image-to-3D)
To modify `gradio_app.py` to add *sdxl-lightning-lora.py* funciton




