## [Jamify](https://github.com/declare-lab/jamify)

### Paper: [JAM: A Tiny Flow-based Song Generator with Fine-grained Controllability and Aesthetic Alignment](https://arxiv.org/abs/2507.20880)
![](https://github.com/declare-lab/jamify/raw/main/jam-teaser.png)
![](https://github.com/declare-lab/jamify/raw/main/jam.png)

### Install
```
git submodule update --init --recursive
pip install -r requirements.txt
pip install -e .
pip install -e externals/DeepPhonemizer
```

---
## [DiffRhythm](https://github.com/ASLP-lab/DiffRhythm)

### Paper
* [DiffRhythm+: Controllable and Flexible Full-Length Song Generation with Preference Optimization](https://arxiv.org/abs/2507.12890)
* [DiffRhythm: Blazingly Fast and Embarrassingly Simple End-to-End Full-Length Song Generation with Latent Diffusion](https://arxiv.org/abs/2503.01183)

![](https://github.com/ASLP-lab/DiffRhythm/raw/main/src/diffrhythm.jpg)

### Install

`git clone https://github.com/ASLP-lab/DiffRhythm.git`<br>
`cd DiffRhythm`<br>

`sudo apt-get install espeak-ng`<br>

`python -m venv .DiffRhythm`<br>
`source .DiffRhythm/bin/activate`<br>

#### For inference using a reference WAV file
`bash scripts/infer_wav_ref.sh`<br>

#### For inference using a text prompt reference
`bash scripts/infer_prompt_ref.sh`<br>

## install requirements
pip install -r requirements.txt
