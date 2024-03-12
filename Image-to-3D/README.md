# Image-to-3D

## [TripoSR](https://github.com/VAST-AI-Research/TripoSR)

### install TripoSR
```
git clone https://github.com/VAST-AI-Research/TripoSR
cd TripoSR
pip install -r requirements.txt
```

### test TripoSR
`python run.py examples/chair.png`<br>

To display `output/0/mesh.obj`: [Online 3D Viewer](https://3dviewer.net/), F3D / 3D Viewer, [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura/)

### Gradio Server UI
`python gradio_app.py`<br>
![](https://github.com/rkuo2000/GenAI/blob/main/assets/TripoSR_Gradio_Server_UI.png?raw=true)

---
## Text-to-3D
Translate + Text-to-Image + TripoSR + Display<br>

### Translate 
`pip install googletrans==4.0.0rc1`<br>
`python gTranslage.py`<br>

### Text-to-Image
`python sdxl-lightning-lora.py`<br>

---
### Display
1. AppInventor2 [3D Model Loader Extension](https://community.appinventor.mit.edu/t/3d-model-loader-extension/43741)

2. Blender

