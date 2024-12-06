# Generative AI
**[生成式人工智慧職缺](https://www.cake.me/campaigns/artificial-intelligence/jobs)** <br>

**[AI 教材](https://rkuo2000.github.io/AI-course/)**<br>
**[AIGC 教材](https://rkuo2000.github.io/AI-course/lecture/2024/08/12/AIGC.html)** <br>
**[GenAI-projects 教材](https://rkuo2000.github.io/GenAI-projects/)** <br>

**範例程式：** `git clone https://github.com/rkuo2000/GenAI`<br>

---
## 1. Text-to-Image 
* [LCM-LoRA.py](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Image/lcm-lora.py)
* [sdxl-base.py](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Image/sdxl-base.py)
* [sdxl-lightning-lora.py](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Image/sdxl-lightning-lora.py)
* [sdxl-lightning-unet.py](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Image/sdxl-lightning-unet.py) 
* [flux.1-dev.py](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Image/flux.1-dev.py)

### Image Creators

#### [Bing-Create tutorial](https://rkuo2000.github.io/GenAI-projects/Bing-Create/)

#### [Midjourney](https://www.midjourney.com/home)

#### [Leonardo.ai](https://app.leonardo.ai/)
![](https://github.com/rkuo2000/GenAI/raw/main/assets/leonardo_abstract_painting_2dogs.png)

#### [civitai](https://civitai.com/)

#### [SeaArt.ai](https://www.seaart.ai/)
<p><img width="50%" height="50%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/SeaArt.ai_ShamppoMix_lingerie_girl.png"></p>

#### [TensorArt](https://tensor.art/)
<p><img width="50%" height="50%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/Tensor.Art_Flux_girl.png"</p>

#### [OpenArt.ai](https://openart.ai/)

#### [goenhance.ai](https://www.goenhance.ai/tutorials)
![](https://github.com/rkuo2000/GenAI/raw/main/assets/GoEnhance.ai.png)
[![](https://markdown-videos-api.jorgenkh.no/youtube/xgU0Xe8HxSE)](https://youtu.be/xgU0Xe8HxSE)

#### [fluxpro.ai](https://www.fluxpro.ai/)
[![](https://markdown-videos-api.jorgenkh.no/youtube/gZTQiyQCgUw)](https://youtu.be/gZTQiyQCgUw)

#### SD 3.5
[ComfyUI Now Supports Stable Diffusion 3.5!](https://blog.comfy.org/sd3-5-comfyui/)<br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/R6dPhx96GNQ)](https://youtu.be/R6dPhx96GNQ)

---
### ComfyUI

#### [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
![](https://github.com/comfyanonymous/ComfyUI/raw/master/comfyui_screenshot.png)

---
#### [本地部署Flux.1 最強文生圖大模型！ Comfyui 一鍵安裝，簡單又方便](https://www.freedidi.com/13266.html)
[![](https://markdown-videos-api.jorgenkh.no/youtube/87TwZ05SSGc)](https://youtu.be/87TwZ05SSGc)

#### Flux1-dev-fp8 model files
* download [flux1-dev-fp8.safetensors](https://huggingface.co/Kijai/flux-fp8/blob/main/flux1-dev-fp8.safetensors)<br>
* download [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors)
* download [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)
* download [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors)
  
```
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
mv ~/Downloads/flux1-dev-fp8.safetensors ~/ComfyUI/models/unet/
mv ~/Downloads/t5xxl_fp8_e4m3fn.safetensors ~/ComfyUI/models/clip/
mv ~/Downloads/clip_l.safetensors ~/ComfyUI/models/clip/
mv ~/Downloads/ae.safetensors ~/ComfyUI/models/vae/
python main.py
```

1. open Browser at `http:127.0.0.1:8188`<br>

2. drag flux_dev_fp8_example.png to browser window to generate the work-flow chart<br>
<p><img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/flux_dev_fp8_example.png"></p>

3. edit text in `CLIP Text Encode (Positive Prompt)`<br>
* [美圖產生提示詞](https://www.freedidi.com/13328.html)<br>

4. click `Queue Prompt` to generate image<br>

#### examples:
```
pretty Asian woman was holding the flowers in her hands, Korean Model, real photo style, full body shot.
```
<p><img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ComfyUI_Flux1_girl_holding_flower.png"></p>

```
One girl, long hair, model, white background, white shirt, khaki Capri pants, khaki loafers, sitting on a stool, lazy pose, slightly tilting head, smiling, Asian beauty, loose-ting clothes, inting clothes , slightly raised foot, half-body shot, Canon R5 camera style, blurred background, indoor, natural light, some sunlight shining on the face，9 : 16.
```
<p><img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ComfyUI_Flux1_longhair_girl_sitting.png"></p>

* 建築設計提示詞<br>
```
A modern office building design with 6 floors. The design language of the building is organic volume, curve design elements, natural leave or flower symbols.
```
<p>
<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ComfyUI_Flux1_building_01.png">
<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ComfyUI_Flux1_building_02.png">
</p>
<p>
<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ComfyUI_Flux1_building_03.png">
<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ComfyUI_Flux1_building_04.png">
</p>

---
### WebUI

#### [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
![](https://github.com/AUTOMATIC1111/stable-diffusion-webui/raw/master/screenshot.png)

---
### Krita
#### 安裝與 ComfyUI 工作流匯入（建築景觀與室內設計應用)
[![](https://markdown-videos-api.jorgenkh.no/youtube/Y99_C0C28UE)](https://youtu.be/k8qoo1hFPic)

#### FLUX.1[dev]模型在Krita完美整合
[![](https://markdown-videos-api.jorgenkh.no/youtube/Y99_C0C28UE)](https://youtu.be/Y99_C0C28UE)

---
## 2. Text-to-3D
**gTranslate + SDXL-Lightning + TripoSR + Blender**<br>

---
## Image-to-3D

### [Zero123+++](https://github.com/SUDO-AI-3D/zero123plus)
* [https://www.kaggle.com/code/rkuo2000/zero123plus](https://www.kaggle.com/code/rkuo2000/zero123plus)<br>
* [https://www.kaggle.com/code/rkuo2000/zero123-controlnet](https://www.kaggle.com/code/rkuo2000/zero123-controlnet)<br>

---
### [TripoSR](https://github.com/VAST-AI-Research/TripoSR)
![](https://favtutor.com/articles/wp-content/uploads/2024/03/TripoSR-Image-to-3D-Objects-Examples.gif)
**Kaggle:** [https://www.kaggle.com/code/rkuo2000/triposr](https://www.kaggle.com/code/rkuo2000/triposr)<br>

---
### Depth Pro
**Code:** [https://github.com/apple/ml-depth-pro](https://github.com/apple/ml-depth-pro)
![](https://github.com/apple/ml-depth-pro/raw/main/data/depth-pro-teaser.jpg)
**Kaggle:** [https://www.kaggle.com/code/rkuo2000/depth-pro](https://www.kaggle.com/code/rkuo2000/depth-pro)<br>

---
## 3. Text-to-Video
### [Tune-A-Video](https://github.com/showlab/Tune-A-Video)
![](https://camo.githubusercontent.com/3a1fe691700facadce50b7dd66641abdc40ce5a97b53e85091d5af0f273481a1/68747470733a2f2f74756e6561766964656f2e6769746875622e696f2f6173736574732f7465617365722e676966)

---
### [Open-VCLIP](https://github.com/wengzejia1/Open-VCLIP/)
![](https://github.com/wengzejia1/Open-VCLIP/raw/main/figures/firstpage.png)

---
### [Dynamic Scene Transformer (DyST)](https://dyst-paper.github.io/)
![](https://dyst-paper.github.io/data/model_fig.png)

---
### [Text-to-Motion-Retrieval](https://github.com/mesnico/text-to-motion-retrieval)
<p><img src="https://github.com/mesnico/text-to-motion-retrieval/raw/main/teaser/example_74.gif"></p>
<p><img src="https://github.com/mesnico/text-to-motion-retrieval/raw/main/teaser/example_243.gif"></p>

---
### [Stable Video Diffusion](https://stability.ai/news/stable-video-diffusion-open-ai-video-model)
![](https://github.com/Stability-AI/generative-models/raw/main/assets/sv4d.gif)

**[SV4D](https://github.com/Stability-AI/generative-models)** <br>
SV4D was trained to generate 40 frames (5 video frames x 8 camera views) at 576x576 resolution

---
### [Runway Gen3](https://runwayml.com/)
[![](https://markdown-videos-api.jorgenkh.no/youtube/SAxZB7wUWYo)](https://youtu.be/SAxZB7wUWYo)

[![](https://markdown-videos-api.jorgenkh.no/youtube/nByslCkykj8)](https://youtu.be/nByslCkykj8)

[Gen-3 Alpha Prompting Guide](https://help.runwayml.com/hc/en-us/articles/30586818553107-Gen-3-Alpha-Prompting-Guide)<br>

---
### [Imagine.Art](https://www.imagine.art/dashboard)<br>
<p><img width="50%" height="50%" src="https://github.com/rkuo2000/GenAI/raw/main/assets/ImagineArt_flying_cat_wearing_superman_suit.png"</p>

[![](https://markdown-videos-api.jorgenkh.no/youtube/ISufT7gYL1o)](https://youtu.be/ISufT7gYL1o)

---
### [RenderNet AI](https://rendernet.ai)
[![](https://markdown-videos-api.jorgenkh.no/youtube/QEh_VJN4ndQ)](https://youtu.be/QEh_VJN4ndQ)
[![](https://markdown-videos-api.jorgenkh.no/youtube/-1qcpu_VuVU)](https://youtu.be/-1qcpu_VuVU)

---
### SORA
[![](https://markdown-videos-api.jorgenkh.no/youtube/iVtqtu6HceI)](https://youtu.be/iVtqtu6HceI)

---
### [Meta MovieGen](https://ai.meta.com/research/movie-gen/)
[![](https://markdown-videos-api.jorgenkh.no/youtube/FHSSx4dUs7E)](https://youtu.be/FHSSx4dUs7E)

---
## 4. Text-to-Avatar
**[GAN 教材](https://rkuo2000.github.io/AI-course/lecture/2024/08/09/GAN.html)** <br>

### [HeyGen](https://www.heygen.com/)
[sample](https://app.heygen.com/share/576aab0e56ee484c91f7eb75ac2338be)<br>

### [Hedra](https://www.hedra.com/)
**[Tutorial](https://rkuo2000.github.io/GenAI-projects/Hedra/)** <br>

### [LivePortrait](https://github.com/KwaiVGI/LivePortrait)
**[Tutorial](https://rkuo2000.github.io/GenAI-projects/LivePortrait/)** <br>
![](https://github.com/KwaiVGI/LivePortrait/raw/main/assets/docs/showcase2.gif)

**[Demo](https://huggingface.co/spaces/KwaiVGI/LivePortrait)** <br>

[![](https://markdown-videos-api.jorgenkh.no/youtube/wBO0VsiWC2s)](https://youtu.be/wBO0VsiWC2s)

---
### [MuskTalk](https://github.com/TMElyralab/MuseTalk)
**[ComfyUI-MuseTalk](https://github.com/chaojie/ComfyUI-MuseTalk)** <br>
<video src=https://github.com/TMElyralab/MuseTalk/assets/163980830/b2a879c2-e23a-4d39-911d-51f0343218e4 controls preload></video>

---
### [artflow.ai](https://app.artflow.ai/)
Charactor Builder<br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/EC9CqEYDS0k)](https://youtu.be/EC9CqEYDS0k)

---
## 5. Text-to-Song 

### [Suno 教學](https://rkuo2000.github.io/GenAI-projects/Suno/)

### [Tuneform](https://tuneform.com/)
[![](https://markdown-videos-api.jorgenkh.no/youtube/_VTfbR5VT4s)](https://youtu.be/_VTfbR5VT4s)

### [Specterr](https://specterr.com/)
[![](https://markdown-videos-api.jorgenkh.no/youtube/MJPuGL-aGzA)](https://youtu.be/MJPuGL-aGzA)

### [Vizzy](https://vizzy.io)
[![](https://markdown-videos-api.jorgenkh.no/youtube/gUko_GnT40g)](https://youtu.be/gUko_GnT40g)

[![](https://markdown-videos-api.jorgenkh.no/youtube/sFaMRk7TGpk)](https://youtu.be/sFaMRk7TGpk)

[![](https://markdown-videos-api.jorgenkh.no/youtube/BvsP4ivkVyM)](https://youtu.be/BvsP4ivkVyM)

---
### ChatGPT(作詞) + SunoAI(作曲) + RVC WebUI (轉換人聲)
[![](https://markdown-videos-api.jorgenkh.no/youtube/9nHbw0eUJeE)](https://youtu.be/9nHbw0eUJeE)

#### [RVC-WebUI開源專案教學](https://gogoplus.net/%E7%BF%BB%E5%94%B1%E6%9C%80%E5%A5%BD%E7%94%A8%E7%9A%84%E9%96%8B%E6%BA%90%E7%A8%8B%E5%BC%8F-rvc-webui-%E5%85%8B%E9%9A%86%E4%BD%A0%E7%9A%84%E8%81%B2%E9%9F%B3/)

**[RVC WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)** <br>

---
## [Generative Speech](https://rkuo2000.github.io/AI-course/lecture/2024/08/09/Generative-Speech.html)
* `python gTTS.py "How are you" en` : generate gTTS.mp3
* `python gT2T.py "How are you" fr` : deep-translator 
* `python gSpeak.py "How are you" fr` : deep-translator, gTTS & Mpg123
  
---
## 6. Text-to-Speech

* **Parler TTS**: `python parler.py`
* **Bark TTA**: `python bark_en.py`, `python bark_cn.py`
* **Coqui TTS**: `python coqui_en.py`, `python coqui_zh.py`
* **text-to-speech**: `python text_to_speech.py`
* **gTTS**: `python gTTS.py "你好?" zh`
* **gTranslate**: `python gTranslate.py`
  
---
## 7. Audio-to-Text (ASR)

### webkitSpeechRecognition
**Blog:** [語音辨識API](https://programmermagazine.github.io/201310/htm/article2.html)<br>

[asr.html](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/asr.html)<br>

[Google Speech Demo](https://www.google.com/intl/en/chrome/demos/speech.html)<br>

---
### Whisper
* [whisper.py](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/whisper.py)
* [whisper-large-v3.py](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/whisper-large-v3.py)
* [faster-whisper.py](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/faster-whisper.py)
* [canary-1b.py](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/canary-1b.py)
<br>

* [qwen_audio.py](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/qwen_audio.py)
* [gemini_audio.py](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/gemini_audio.py)

---
### local ASR+LLM Server running on GPU
1. **run server on local PC (with GPU):** `python whisper_llm_server.py`<br>
2. **Generate audio file**: `python ../gTTS.py "Hello, how are you?" en`<br>
3. **Post Audio to Server**: `python post_audio.py`<br>

---
## 8. Text-to-Text (LLMs)

**[Large Language Models 教材](https://rkuo2000.github.io/AI-course/lecture/2024/08/15/LLM.html)** <br>
**[Prompt Engineering 教材](https://rkuo2000.github.io/AI-course/lecture/2024/08/15/Prompt-Engineering.html)** <br>

`git clone https://github.com/rkuo2000/GenAI`<br>
`cd GenAI/Text-to-Text`<br>

* `python gpt4free.py` (gpt-3.5-turbo)
* `python gpt4all_prompting.py`
* `python LLM_prompting.py`
* [colab_LLM_prompting.ipynb](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/colab_LLM_prompting.ipynb) (on Colab T4) 

#### local LLM Server & Client
* `python llm_server.py` (on GPU)
* `python post_text.py`  (on PC)

---
### Colab running LLM Server
* [colab_pyNgrok_LLM_server](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/colab_pyNgrok_LLM_Server.ipynb) (on Colab T4)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/pyngrok_LLM_Server_fastapi.png?raw=true)
* [post-text client](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/post_text.py) (on PC)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/pyngrok_post_text.png?raw=true)

---
### Colab running ASR+LLM Server
1. **Open [colab](https://colab.research.google.com) to run [pyngrok_Whisper_LLM_Server.ipynb](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/pyngrok_Whisper_LLM_Server.ipynb)** on Colab T4
2. **Generate audio file**: `python ../gTTS.py "Hello, how are you?" en`<br>
3. **Post Audio to Server**: `python post_audio.py`<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/post_audio.png?raw=true)

---
### [Ollama](https://ollama.com/)

#### [ollama library](https://ollama.com/library)
`ollama list`<br>
`ollama run llama3.2`<br>

#### ollama chat/generate
* `python ollama_chat.py`
* `python ollama_stream.py` (print text in streaming mode)
* `python ollama_curl.py`

#### ollama speak
* `python ollama_speak.py` (ollama generated text, gTTS to speech, then mpg123 to speak)
* `python ollama_speak_t2t.py` (ollama generated text, gTTS to speech, deep-translator to zh-TW, mpg123 to speak)

---
### [LM Studio](https://lmstudio.ai/)
![](https://github.com/rkuo2000/GenAI/blob/main/assets/LM_Studio_0.3.3.png?raw=true)

---
### [Gemini API](https://ai.google.dev/api/generate-content?hl=zh-tw)
**[get Gemini API Key](https://aistudio.google.com/app/apikey)** <br>

---
#### [gemini.html](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/gemini.html)
![](https://github.com/rkuo2000/GenAI/blob/main/assets/Gemini_html.jpg?raw=true)  

---
#### [Gemini_Talk App 教學](https://rkuo2000.github.io/GenAI-projects/AI2_Gemini_Talk_app/)
MIT App Inventor 2 example for using Google Gemini<br>  
* Download [Gemini_Talk.aia ](https://github.com/rkuo2000/GenAI/blob/main/Gemini_Talk.aia), import to [[ai2.mit](https://ai2.appinventor.mit.edu/)](https://ai2.appinventor.mit.edu/)
  
* [Get API Key](https://aistudio.google.com/app/apikey) and put into the `blank`<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/Gemini_Talk_edit_API_key.png?raw=true)

* Build apk, download & install to run on smartphone<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/Gemini_Talk.jpg?raw=true)

(三星手機使用三星文字轉語音引擎應用程式, 語言設繁體中文會講不出話, 要改成簡體中文, 或使用英文）

---
## 9. LLM Fine-Tuning
**[LLM Fine-Tuning 教材](https://rkuo2000.github.io/AI-course/lecture/2024/08/17/LLM-FineTuning.html)** <br>

### PEFT
[fine-tune-gemma-7b-it-for-sentiment-analysis](https://www.kaggle.com/code/rkuo2000/fine-tune-gemma-7b-it-for-sentiment-analysis)<br>
[fine-tune-llama-3-for-sentiment-analysis](https://www.kaggle.com/code/rkuo2000/fine-tune-llama-3-for-sentiment-analysis)<br>

### LoRA
[fine-tune-gemma-models-in-keras-using-lora](https://www.kaggle.com/code/rkuo2000/fine-tune-gemma-models-in-keras-using-lora)<br>

### exmaples
* [https://www.kaggle.com/code/tommyadams/fine-tuning-tinyllama](https://www.kaggle.com/code/tommyadams/fine-tuning-tinyllama)<br>
* [https://www.kaggle.com/code/ejaz22/finetune-tinyllama-addr-extraction](https://www.kaggle.com/code/ejaz22/finetune-tinyllama-addr-extraction)<br>
* [https://www.kaggle.com/code/schock/training-tinyllama-for-tool-calling](https://www.kaggle.com/code/schock/training-tinyllama-for-tool-calling)<br>

---
## 10. Image-to-Text (VLM)

---
### examples
* [python llava-1.5-7b-hf.py](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/llava-1.5-7b-hf.py)
* [python llava-1.6-7b-hf.py](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/llava-1.6-7b-hf.py)
* [forence-2.py](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/florence-2.py)
* [phi-3.5-vision.py](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/pixtral.py)
* [pixtral.py](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/pixtral.py)
* [llama-3.2-vision.py](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/llama-3.2-vision.py)

---
### VLM servers
For running server, (use one of the following)<br>
1. `python llava_server.py`
2. `python llava_next_server.py`
3. `python phi3-vision_server.py`

For running client, (post image & text to VLM server)<br>
`python post_imgtxt.py images/barefeet1.jpg`<br>

---
### ASR + VLM servers
1. `python whisper_llava_server.py`
2. `python ../gTTS.py "這是什麼有名的台南美食?" zh` (TTS)<br>
3. `python post_imgau.py` (client)<br>

---
### [Gemini API](https://ai.google.dev/api/generate-content?hl=zh-tw)
* `python gemini_image.py`<br>
* `python gemini_jpg2csv.py`<br>

---
## 11. RAG 
**[RAG 教材](https://rkuo2000.github.io/AI-course/lecture/2024/08/18/RAG.html)** <br>
![](https://blogs.mathworks.com/deep-learning/files/2024/01/rag.png)

### Sampe Codes
* [https://www.kaggle.com/code/rkuo2000/langchain-rag-chromadb](https://www.kaggle.com/code/rkuo2000/langchain-rag-chromadb)
* [https://www.kaggle.com/code/rkuo2000/llm-llamaindex](https://www.kaggle.com/code/rkuo2000/llm-llamaindex) = LlamaIndex-RAG-pdf
* Langchain-RAG-text.ipynb
* Langchain-ReAct.ipynb
* LlamaIndex-RAG-pdf.ipynb
* LlamaIndex-RAG-pdf-community.ipynb
* LlamaIndex-RAG-pdf-community.py

---
### [RAG Builder](https://github.com/KruxAI/ragbuilder)

---
## 12. Agent
**[Agent 教材](https://rkuo2000.github.io/AI-course/lecture/2024/10/16/Agents.html)** <br>

### [openai/swarm](https://github.com/openai/swarm)
![](https://github.com/openai/swarm/raw/main/assets/swarm_diagram.png)

**Kaggle:** [rkuo2000/swarm-llama3-groq](https://www.kaggle.com/code/rkuo2000/swarm-llama3-groq)<br>
**Colab:** [colab_Swarm_Llama3_Groq.ipynb](https://github.com/rkuo2000/GenAI/blob/main/Agent/colab_Swarm_Llama3_Groq.ipynb)<br>

---
## 參考書籍

### [LLM 大型語言模型的絕世祕笈](https://www.tenlong.com.tw/products/9786263339293)
![](https://cf-assets2.tenlong.com.tw/products/images/000/213/023/webp/9786263339293.webp?1721374719)

* [中二技能翻譯](https://github.com/penut85420/SpellTrans) <br>
這是一個 LangChain 練習專案，透過 LLM 結合 Riot API 取得的英雄技能翻譯，以 Few-Shot Prompt 的方式獲得中二的技能翻譯。<br>
![](https://camo.githubusercontent.com/b21a9836a321a5830eccebe49abd558441d895b6f39fa6dce2f725fd0049e908/68747470733a2f2f692e696d6775722e636f6d2f386b61476e50712e706e67)

---
### [最強 AI 投資分析：打造自己的股市顧問機器人，股票趨勢分析×年報解讀×選股推薦×風險管理](https://www.tenlong.com.tw/products/9789863127727)
![](https://cf-assets2.tenlong.com.tw/products/images/000/195/999/webp/9789863127727_%E5%A4%A9%E7%93%8F.webp?1699843474)

