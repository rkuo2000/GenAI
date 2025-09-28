from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolo11n.pt")

# Export the model to TensorRT
# create yolo11n.engine
#model.export(format="engine") # FP32
#model.export(format="engine",half=True) # FP16
model.export(format="engine",int8=True) # INT8
