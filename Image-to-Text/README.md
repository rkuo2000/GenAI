# Image-to-Text

## [LLaVA](https://llava-vl.github.io/)

### LLaVA installation

* install miniconda3 for virtual env
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
source ~/miniconda3/bin/activate
conda init
```

* create virtual env & install LLaVA
```
conda create -n LLaVA_env
conda activate LLaVA_env
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
pip install -e .
```

### LLaVA Server

* run serve controller<br>
`python -m llava.serve.controller --host 0.0.0.0 --port 10000`<br>

* run Model-worker<br>
`python -m llava.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40000 --worker :http://localhost:40000 --model-path liuhaotian/llava-v1.5-7b`<br>

* run GUI-server<br>
`python -m llava.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload`<br>

* Open Browser at `127.0.0.1:7860`<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/LLaVA_Gradio_Server_UI.png?raw=true)

*Drag a picture, and put a text as prompt, then click [Send]*<br>

