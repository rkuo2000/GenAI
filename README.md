# Generative AI sample codes

## Audio-to-Text
* `post_audio.py` : HTTP Post audio file to a http-server
* `whisper_server.py` : HTTP server to receive audio file and transcribe to text
* `whisper_llm_server.py` : HTTP server to transcribe audio file to text, and text-to-text by calling a LLM model

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
* To run
`python run.py examples/chair.png`<br>
* To view .obj file with F3D viewer, or Blender (Game Engine), or Slicer (3D-printer)


