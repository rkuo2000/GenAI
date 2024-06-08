# Image-to-Text
---
## [LLaVA 1.5](https://llava-vl.github.io/)

### post image+text to llava_server
* Server: `python llava_server.py`
* Client: `python post_imgtxt.py`

### post image+audio to whisper_llava_server
* Server: `python whisper_llava_server.py`
* Client: `python post_imgau.py`

### Demo
**Download a picture:** Tainan_BeefSoup.jpg<br>
<p><img width="50%" height="50%" src="https://github.com/rkuo2000/GenAI/blob/main/Image-to-Text/images/Tainan_BeefSoup.jpg?raw=true"></p>

**Generate Audio file:** gTTS.mp3<br>
`python ../gTTS.py "這是什麼有名的台南美食?" zh`<br>

#### Send Image & Audio to VLM server
`python post_imgau.py`<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/post_imgau.png?raw=true)

---
## LLaVA 1.6
model: "llava-hf/llava-v1.6-vicuna-7b-hf"<br>

### test
`python llava-1.6-7b-hf.py images/Tainan_BeefSoup.jpg`<br>

### post image+audio to whisper_llava_server
* Server: `python whisper_llava_next_server.py`
* Client: `python post_imgau.py`
