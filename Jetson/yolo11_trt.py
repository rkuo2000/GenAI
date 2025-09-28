from ultralytics import YOLO

#model = YOLO("yolo11n.pt")
#model.export(format="engine")

trt_model = YOLO("yolo11n.engine")

#results = onnx_model("https://ultralytics.com/images/bus.jpg")
results = onnx_model("bus.jpg")

for result in results:
    result.show()
