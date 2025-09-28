from ultralytics import YOLO

model = YOLO("yolo11n.pt")

#results = model("https://ultralytics.com/images/bus.jpg")
results = model("bus.jpg")

for result in results:
    result.show()
