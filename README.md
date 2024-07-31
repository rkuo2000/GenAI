# Generative AI - sample codes
* `gTTS.py` : to generate gTTS.mp3
* `gT2T.py` : google translate

---
## Text-to-Text (LLMs)

### LLM prompting
* `python gpt4free.py` (gpt-3.5-turbo)
* `python gpt4all_prompting.py`
* `python LLM_prompting.py`
* [colab_LLM_prompting.ipynb](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/colab_LLM_prompting.ipynb) (on Colab T4) 

---
### LLM Server & Client
* `python llm_server.py` (on GPU)
* `python post_text.py`  (on PC)

---
### Colab's LLM Server & Client
* [colab_pyNgrok_LLM_server](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/colab_pyNgrok_LLM_Server.ipynb) (on Colab T4)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/pyngrok_LLM_Server_fastapi.png?raw=true)
* [post-text client](https://github.com/rkuo2000/GenAI/blob/main/Text-to-Text/post_text.py) (on PC)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/pyngrok_post_text.png?raw=true)

---
### Ollama
`ollama list`<br>
`ollama run llama3.1`<br>

#### ollama chat/generate
* `python ollama_chat.py`
* `python ollama_stream.py` (print text in streaming mode)
* `python ollama_curl.py`

#### ollama speak
* `python ollama_speak.py` (ollama generated text, gTTS to speech, then mpg123 to speak)
* `python ollama_speak_t2t.py` (ollama generated text, gTTS to speech, deep-translator to zh-TW, mpg123 to speak)
  
---
## Audio-to-Text

### local ASR+LLM Server (on your PC+GPU)
1. **run server on local PC (on your PC+GPU):** `python whisper_llm_server.py`<br>
2. **Generate audio file**: `python ../gTTS.py "Hello, how are you?" en`<br>
3. **Post Audio to Server**: `python post_audio.py`<br>

---
### Colab ASR+LLM Server (on Colab T4)
1. **Open [colab](https://colab.research.google.com) to run [pyngrok_Whisper_LLM_Server.ipynb](https://github.com/rkuo2000/GenAI/blob/main/Audio-to-Text/pyngrok_Whisper_LLM_Server.ipynb)** on Colab T4
2. **Generate audio file**: `python ../gTTS.py "Hello, how are you?" en`<br>
3. **Post Audio to Server**: `python post_audio.py`<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/post_audio.png?raw=true)

---
## Image-to-Text (VLM)

### VLM servers
For running server, (use one of the following)<br>
1. `python llava_server.py`
2. `python llava_next_server.py`
3. `python phi3-vision_server.py`

For running client, (post image & text to VLM server)<br>
`python post_imgtxt.py images/barefeet1.jpg`<br>

### ASR + VLM servers
1. `python whisper_llava_server.py`
2. `python ../gTTS.py "這是什麼有名的台南美食?" zh` (TTS)<br>
3. `python post_imgau.py` (client)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/images/Tainan_BeefSoup.jpg?raw=true)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/post_imgau.png?raw=true)

* Whisper+LLaVA Server (ASR+VLM)<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/whisper_llava_server.png?raw=true)

---
## Text-to-Speech
* **Parler TTS**: `python parler.py`
* **Bark TTA**: `python bark_en.py`, `python bark_cn.py`
* **Coqui TTS**: `python coqui_en.py`, `python coqui_zh.py`
* **text-to-speech**: `python text_to_speech.py`
* **gTTS**: `python gTTS.py "你好?" zh`
* **gTranslate**: `python gTranslate.py`

---
## Text-to-Image 
* `sdxl-base.py` - run SDXL-base model to input text and generate an image
* `sdxl-lightning-lora.py` - run SDXL-Lightning with LoRA model to use text to generate an image
* `sdxl-lightning-unet.py` - run SDXL-Lightning with UNet model to use text to generate an image

---
## Image-to-3D

### TripoSR
![](https://favtutor.com/articles/wp-content/uploads/2024/03/TripoSR-Image-to-3D-Objects-Examples.gif)

### Text-to-3D
**gTranslate + SDXL-Lightning + TripoSR + AppInventor2**<br>
