# Generative AI
* python  == 3.12.3
* torch   == 2.9.0+cu128
* torchvision == 0.24.0+cu128
* torchao == 0.14.1

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
## 2. [Generative Video](https://rkuo2000.github.io/AI-course/lecture/2025/09/12/Generative-Video.html)

### Sora2
[![](https://markdown-videos-api.jorgenkh.no/youtube/5XgvjKV1iEw)](https://youtu.be/5XgvjKV1iEw) 

### Veo3.1
[![](https://markdown-videos-api.jorgenkh.no/youtube/PL_izvWJVLU)](https://youtu.be/PL_izvWJVLU)

---
### Text-to-Video, Image-to-Video
**[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** <br>

**[ComfyUI - WAN2.2](https://docs.comfy.org/tutorials/video/wan/wan2_2)** <br>

---
### Animate
**[ComfyUI - Wan2.2 Animate](https://docs.comfy.org/tutorials/video/wan/wan2-2-animate)** <br>

---
### Audio-drvien Video
**[ComfyUI - Wan2.2 S2V](https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v)** <br>

**[ComfyUI - Wan2.1 InfiniteTalk 讓圖片、影片生成的人物完美對應口型](https://home.gamer.com.tw/artwork.php?sn=6197438)** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/C64RibgbgTg)](https://youtu.be/C64RibgbgTg) 

1) Text-to-Image  : `Grok.com/imagine`<br>
2) Lyrics-to-Song : `Suno.com`<br>
3) Image-to-Video : `ComfyUI + Wan2.1 Video + InfiniteTalk`
   
[![](https://markdown-videos-api.jorgenkh.no/youtube/vTt7lkq-p9A)](https://youtu.be/vTt7lkq-p9A) 

---
#### I2T -> T2I -> I2V
**[ComfyUI_Qwen3-VL-Instruct](https://github.com/IuvenisSapiens/ComfyUI_Qwen3-VL-Instruct)** <br>

[![](https://markdown-videos-api.jorgenkh.no/youtube/OZk4yhlFJhk)](https://youtu.be/OZk4yhlFJhk) 

---
## 3. [Generative Song](https://rkuo2000.github.io/AI-course/lecture/2025/09/10/Generative-Song.html)

### [DiffRhythm](https://github.com/ASLP-lab/DiffRhythm)

### [Jamify](https://github.com/declare-lab/jamify) 
[https://www.kaggle.com/code/rkuo2000/jamify](https://www.kaggle.com/code/rkuo2000/jamify)

### [ACE-step](https://github.com/ace-step/ACE-Step): [ComfyUI ACE-step](https://github.com/billwuhao/ComfyUI_ACE-Step)

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

### [TalkMateAI](https://github.com/kiranbaby14/TalkMateAI)
[![](https://markdown-videos-api.jorgenkh.no/youtube/dE_8TXmp2Sk)](https://youtu.be/dE_8TXmp2Sk) 

---
### [LipSync-Avatar](https://github.com/android-iceland/LipSync-Avatar)
[![](https://markdown-videos-api.jorgenkh.no/youtube/w8Qwrh8t0n4)](https://youtu.be/w8Qwrh8t0n4) 

