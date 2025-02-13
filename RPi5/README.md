# GenAI LLMs & EdgeAI devices 
自強基金會 WiFi <br>
```
SSID: TCFSTWIFI.ALL
Pass: 035623116
```

## 1. AI 介紹

### [AI 簡介](https://rkuo2000.github.io/AI-course/lecture/2024/08/01/AI-Brief.html)

### [AI 硬體介紹](https://rkuo2000.github.io/AI-course/lecture/2024/08/01/AI-Hardwares.html)

---
## 2. EdgeAI on RPi5

### RPi5 套件

[樹莓派5 Raspberry Pi 5 Model B 8G 全配套件](https://shopee.tw/product/143152281/25051137272?d_id=475b0&uls_trackid=51vt6ret01go&utm_content=B4YYSAxc5NBjtacxA4J4jEiErVD)<br>
![](https://down-tw.img.susercontent.com/file/tw-11134207-7rasc-m5b7sf03lbg6b0@resize_w450_nl.webp)

### RPi5 OS 安裝
1. 下載image燒錄至SD卡（32GB以上)
**[Raspberry Pi OS (64-bit)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)** <br>
2. [使用 Raspberry Pi Imager安裝](https://www.raspberrypi.com/software/)
3. [如何在 Raspberry Pi 5 使用 M.2 HAT+ 從 NVMe SSD 啟動](https://piepie.com.tw/55084/how-to-boot-from-nvme-ssd-using-m.2-hat-plus-on-raspberry-pi-5)

### [Raspberry Pi Connect](https://www.raspberrypi.com/software/connect/)
![](https://assets.raspberrypi.com/static/abae19beca53f018d9c434ddee214cd9/38f47/screenshot.webp)

```
sudo apt update
sudo apt full-upgrade

sudo sudo apt install rpi-connect

```
**Turn On Raspberry Pi Connect** <br>
![](https://www.raspberrypi.com/documentation/services/images/turn-on-connect.png?hash=f03f4519e48a4b6e5b1580d3f905f61a)

**Then, Add device** <br>
![](https://www.raspberrypi.com/documentation/services/images/screen-sharing-in-progress.png?hash=5b58232d27f2c31b4b324f1187d80057)

---
## 3. OpenCV in Python

### [Python Programming](https://www.programiz.com/python-programming)
### [Python Tutorial](https://www.w3schools.com/python/python_intro.asp)

### [OpenCV for Python](https://rkuo2000.github.io/AI-course/lecture/2024/08/02/OpenCV-Python.html)

---
## 4. YOLOv11
**[A Comprehensive Guide to YOLOv11 Object Detection](https://www.analyticsvidhya.com/blog/2024/10/yolov11-object-detection/)** <br>

### YOLO演化時間軸
![](https://cdn.analyticsvidhya.com/wp-content/uploads/2024/10/TimelineCycle.webp)

### [YOLOv11 Ultralytics](https://github.com/ultralytics/ultralytics)
![](https://raw.githubusercontent.com/ultralytics/assets/refs/heads/main/yolo/performance-comparison.png)
![](https://github.com/rkuo2000/AI-course/blob/main/images/YOLOv11_Ultralytics_features.png?raw=true)

---
### YOLOv11 Architecture
![](https://miro.medium.com/v2/resize:fit:1200/1*L8rMuwurmyBH1ixIqcrMSQ.png)

---
### [Kaggle YOLOv11 example](https://www.kaggle.com/code/rkuo2000/yolov11/)

`!pip install ultralytics`<br>

---
### YOLO11 example code

```
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="coco8.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)
# Perform object detection on an image
results = model("input/image.jpg")
results[0].show()
```

### [YOLO11+Camera+Speak example](https://github.com/rkuo2000/GenAI/blob/main/RPi5/yolo11_cam_speak.py)

---
### YOLO data format
![](https://cdn.prod.website-files.com/5f6bc60e665f54545a1e52a5/614cd66c5d86816d057ef364_yolov5-coordinates.jpeg)

**001.txt**<br>
```
1 0.617 0.3594420600858369 0.114 0.17381974248927037
1 0.094 0.38626609442060084 0.156 0.23605150214592274
1 0.295 0.3959227467811159 0.13 0.19527896995708155
1 0.785 0.398068669527897 0.07 0.14377682403433475
1 0.886 0.40879828326180256 0.124 0.18240343347639484
1 0.723 0.398068669527897 0.102 0.1609442060085837
1 0.541 0.35085836909871243 0.094 0.16952789699570817
1 0.428 0.4334763948497854 0.068 0.1072961373390558
1 0.375 0.40236051502145925 0.054 0.1351931330472103
1 0.976 0.3927038626609442 0.044 0.17167381974248927
```

**data.yaml**<br>
```
train: ../train/images
val: ../valid/images

nc: 3
names: ['head', 'helmet', 'person']
```

**convert coco format**<br>
```
from ultralytics.data.converter import convert_coco

convert_coco(labels_dir="path/to/coco/annotations/")
```

---
## 5. ollama

### [ollama download](https://ollama.com/download)
`curl -fsSL https://ollama.com/install.sh | sh`<br>

### [ollama models](https://ollama.com/search)

* **deepseek-r1**: DeepSeek's first-generation of reasoning models with comparable performance to OpenAI-o1, including six dense models distilled from DeepSeek-R1 based on Llama and Qwen.
* **llama3.3** : New state of the art 70B model. Llama 3.3 70B offers similar performance compared to the Llama 3.1 405B model.
* **phi4** : Phi-4 is a 14B parameter, state-of-the-art open model from Microsoft.
* **mistral** : The 7B model released by Mistral AI, updated to version 0.3
* **tinyllama** : The TinyLlama project is an open endeavor to train a compact 1.1B Llama model on 3 trillion tokens.

---
### [Prompt Engineering](https://rkuo2000.github.io/AI-course/lecture/2024/08/15/Prompt-Engineering.html)
![](https://github.com/rkuo2000/AI-course/blob/main/images/chatgpt_cheat_sheet_v2.jpg?raw=true)

---
## 6. GenAI APIs

### Google Gemini
[Gemini API](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-tw#gemini-api)<br>
`response = client.models.generate_content(model="gemini-2.0-flash-exp", contents="How does RLHF work?")`<br>

[Google AI Studio models](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-tw#google-ai-studio)<br>

### example codes
* [gemini_image.py](https://github.com/rkuo2000/GenAI/blob/main/RPi5/gemini_image.py)<br>
* [gemini_image_speak.py](https://github.com/rkuo2000/GenAI/blob/main/RPi5/gemini_image_speak.py)<br>
* [test_gpio.py](https://github.com/rkuo2000/GenAI/blob/main/RPi5/test_gpio.py)<br>
* [gpio_gemini_cam_speak.py](https://github.com/rkuo2000/GenAI/blob/main/RPi5/gpio_gemini_cam_speak.py)<br>

---
## 7. EdgeAI on Smartphone

### [App Inventor 2](https://rkuo2000.github.io/GenAI-projects/AppInventor2_Intro/)

### [Gemini Talk](https://rkuo2000.github.io/GenAI-projects/AI2_Gemini_Talk_app/)

---
### [PocketPal](https://github.com/a-ghorbani/pocketpal-ai)
[Get it on Google Play](https://play.google.com/store/apps/details?id=com.pocketpalai)<br>









