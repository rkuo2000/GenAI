# Generative AI
* python==3.12.3
* torch==2.9.1+cu128
* triton==3.5.1
* torchvision==0.24.1+cu128
* torchao==0.15.0
* torchaudio==2.10.0+cu128
* transformers==4.57.6
* tokenizers==0.22.2
* accelerate==1.12.0
* flash-attn==2.8.3+cu128
* peft==0.18.1

---
### ComfyUI
**[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** <br>
`git clone https://github.com/comfyanonymous/ComfyUI`<br>
`cd ComfyUI/custom_nodes`<br>

**Custom Nodes**:<br>
* [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)
`git clone https://github.com/ltdrdata/ComfyUI-Manager`<br>

* [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
`git clone https://github.com/kijai/ComfyUI-WanVideoWrapper`<br>


**To run ComfyUI**<br>
`cd ~/ComfyUI`<br>
`python main.py`<br>

GUI: http://127.0.0.1:8188

---
## 1. [Generative Image](https://rkuo2000.github.io/AI-course/lecture/2025/09/11/Generative-Image.html)

[![](https://markdown-videos-api.jorgenkh.no/youtube/awl4vLMbUP4)](https://youtu.be/awl4vLMbUP4) [![](https://markdown-videos-api.jorgenkh.no/youtube/93fYXstDrjc)](https://youtu.be/93fYXstDrjc)

### [NanoBanana](https://aistudio.google.com/prompts/new_chat)
**Prompt**: <br>
```
請生成年輕女性
臉部特徵與妝容
​五官: 擁有清秀、柔和的五官，臉型屬於鵝蛋臉或偏瓜子臉。豐滿上圍凸出
​眼睛: 眼神清澈且專注，是單眼皮或內雙眼皮，帶有自然的東方美感。
​膚質/妝容: 膚色白皙、透亮，妝容非常自然、輕薄，呈現出**「偽素顏」或「裸妝」的效果，強調肌膚的光澤感和無瑕疵**。
​💇 髮型
​髮色/髮質: 髮色是深棕色或自然黑，髮質看起來柔順且有光澤。
​造型: 髮型是半紮式馬尾（或公主頭），將上半部的頭髮向後梳起，展現出俐落感；同時保留了幾縷髮絲自然地垂落在臉頰兩側，增添了柔美的氣息。
​👚 服裝與整體風格
​服裝: 穿著一件米色或淺裸色的上衣，材質似乎是輕薄的針織或有細紋理的布料，
​風格: 整體風格是清新、自然、優雅，模特兒的形象。
​🌟 簡潔重點總結
​她是一位外型清新、氣質溫柔的女性。擁有白皙透亮的自然裸妝，搭配柔順的深棕色半紮髮，整體散發出優雅而專注的氛圍。在咖啡廳
```
<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/blob/main/assets/NanoBanana_lady.png?raw=true">

---
### [Imagen4](https://aistudio.google.com/prompts/new_image?model=imagen-4.0-generate-001)
**Prompt**:<br>
```
A beautiful young woman with long, voluminous, wavy brown hair and hazel eyes, looking thoughtfully to the side.
She is illuminated by soft, natural light coming from a nearby window with sheer curtains. She is wearing a simple, beige off-the-shoulder top.
The mood is serene and pensive. The style should be a photorealistic portrait with a shallow depth of field, creating a soft, blurred background.
```
<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/blob/main/assets/Imagen4_girl.png?raw=true">


---
### [Grok.imagine](https://grok.com/imagine)
**Prompt**: 
```
Photorealistic close-up portrait of a young East Asian female singer (K-pop idol aesthetic) on a dark stage.
big eyes with thick lips wearing a black off-the-shoulder top with spaghetti straps. Her light brown hair is styled in wavy and curry.
She is holding a professional stage microphone and singing with a focused, emotional expression.
Dramatic, high-contrast volumetric lighting, strong spotlight isolating the subject, deep shadows, blue/black background.
Cinematic shot, 8k, hyperdetailed, shallow depth of field, aspect ratio 9:16
```

<img width="25%" height="25%" src="https://github.com/rkuo2000/GenAI/blob/main/assets/Grok_Kpop_girl.jpg?raw=true">

---
### [Z-Image Turbo](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo)
**Model**: [Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo/tree/main/split_files)<br>
<iframe width="514" height="289" src="https://www.youtube.com/embed/qHqRSXB4xPQ" title="ComfyUI 結合 Z-Image Turbo 全攻略｜不可思議的6B本機生圖模型，20秒出圖、支援中文！本機部署實測" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
### RED-Zimage 1.5
**Model**: [https://civitai.com/models/958009/redcraft-or-redzimage-or-updated-dec03-or-latest-red-z-v15](https://civitai.com/models/958009/redcraft-or-redzimage-or-updated-dec03-or-latest-red-z-v15)<br>
**Blog**:[RED-Zimage 1.5 Review: Finally, Real AI Photos?](https://z-image.ai/zh/blog/red-zimage-1-5-review)<br>
<iframe width="533" height="289" src="https://www.youtube.com/embed/DOkeQdxNjaU" title="50.ComfyUI完整指南：ComfyUI 新王者！REDZimage 1.5 全面超越 Zimage Turbo，寫實效果再進化！" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
## 2. [Generative Video](https://rkuo2000.github.io/AI-course/lecture/2025/09/12/Generative-Video.html)

### Sora2
[![](https://markdown-videos-api.jorgenkh.no/youtube/5XgvjKV1iEw)](https://youtu.be/5XgvjKV1iEw) 

### Veo3.1
[![](https://markdown-videos-api.jorgenkh.no/youtube/PL_izvWJVLU)](https://youtu.be/PL_izvWJVLU)

### Wan2.2
**[ComfyUI - WAN2.2](https://docs.comfy.org/tutorials/video/wan/wan2_2)** <br>

### [LTX-2.3](https://ltx.io/model/ltx-2-3)
[![](https://markdown-videos-api.jorgenkh.no/youtube/ZlqZEb8uBDM)](https://youtu.be/ZlqZEb8uBDM) 

---
## 3. [Generative Song](https://rkuo2000.github.io/AI-course/lecture/2025/09/10/Generative-Song.html)

### [DiffRhythm](https://github.com/ASLP-lab/DiffRhythm)

### [Jamify](https://github.com/declare-lab/jamify) 
[https://www.kaggle.com/code/rkuo2000/jamify](https://www.kaggle.com/code/rkuo2000/jamify)

---
### [ACE-step](https://github.com/ace-step/ACE-Step)
**[ComfyUI ACE-step](https://github.com/billwuhao/ComfyUI_ACE-Step)** <br>
![](https://github.com/billwuhao/ComfyUI_ACE-Step/blob/main/images/2025-05-10_19-26-46.png?raw=true)

---
### [Suno](https://suno.com/home)
[![](https://markdown-videos-api.jorgenkh.no/youtube/WYIvrVZNm5M)](https://youtu.be/WYIvrVZNm5M) 

#### [Suno小標籤提示詞1.pdf](https://github.com/rkuo2000/GenAI/blob/main/assets/Suno%E5%B0%8F%E6%A8%99%E7%B1%A4%E6%8F%90%E7%A4%BA%E8%A9%9E1.pdf)

---
## 4. [Generative Speech](https://rkuo2000.github.io/AI-course/lecture/2025/09/09/Generative-Speech.html)

### [Spark-TTS](https://github.com/SparkAudio/Spark-TTS) 
[https://kaggle.com/code/rkuo2000/Spark-TTS](https://kaggle.com/code/rkuo2000/Spark-TTS) ~ [spark.mp3](https://rkuo2000.github.io/read-audio/?p=https://github.com/rkuo2000/GenAI/raw/refs/heads/main/assets/spark.mp3)<br>

### [Index-TTS2](https://github.com/index-tts/index-tts) 
[https://kaggle.com/code/rkuo2000/Index-TTS2](https://kaggle.com/code/rkuo2000/Index-TTS2) ~ [gen.mp3](https://rkuo2000.github.io/read-audio/?p=https://github.com/rkuo2000/GenAI/raw/refs/heads/main/assets/gen.mp3)<br>

### [FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2)
![](https://github.com/rkuo2000/GenAI/blob/main/assets/FireRedTTS2_gradio_monologue.png?raw=true) 

[audio.mp3](https://rkuo2000.github.io/read-audio/?p=https://github.com/rkuo2000/GenAI/raw/refs/heads/main/assets/audio.mp3)<br>

---
## 5. Talking Avatar

### [First Order Motion Model for Image Animation](https://github.com/AliaksandrSiarohin/first-order-model)
![](https://github.com/AliaksandrSiarohin/first-order-model/raw/master/sup-mat/relative-demo.gif)

---
### [LipSync-Avatar](https://github.com/android-iceland/LipSync-Avatar)
[![](https://markdown-videos-api.jorgenkh.no/youtube/w8Qwrh8t0n4)](https://youtu.be/w8Qwrh8t0n4) 

---
### [TalkMateAI](https://github.com/kiranbaby14/TalkMateAI)
[![](https://markdown-videos-api.jorgenkh.no/youtube/dE_8TXmp2Sk)](https://youtu.be/dE_8TXmp2Sk) 

---
## 6. Image-to-3D

### Hunyuan3D
**Paper**: [Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details](https://arxiv.org/abs/2506.16504)<br>
**Code**: [https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1)<br>
![](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/raw/main/assets/images/pipeline.png)

**[ComfyUI - Hunyuan3D 2.1](https://docs.comfy.org/tutorials/3d/hunyuan3D-2)** <br>
![](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33c158fcfb133560674aa56bfdb5087d)
