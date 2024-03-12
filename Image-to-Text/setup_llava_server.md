## LLaVA server

### LLaVA installation
`cd ~`<br>
`conda create -n LLaVA_env`<br>
`conda activate LLaVA_en`<br>
`git clone https://github.com/haotian-liu/LLaVA.git`<br>
`cd LLaVA`<br>
`pip install -e .`<br>

### run API-server: LLaVA serve controller at port 10000 
`python -m llava.serve.controller --host 0.0.0.0 --port 10000`<br>

### run Model-worker: LLaVA model-worker at port 40000 
`python -m llava.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40000 --worker :http://localhost:40000 --model-path liuhaotian/llava-v1.5-7b`<br>

### run GUI-server (webUI to LLaVA server-controller at 10000 
`python -m llava.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload`<br>

### Open Browser at 127.0.0.1/7860
Gradio web server GUI will show up !!!
Drag a picture, and put a text as prompt, then click [Send]
