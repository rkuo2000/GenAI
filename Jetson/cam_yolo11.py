#!/home/user/venv/bin/python

import os
import cv2
from PIL import Image
from ultralytics import YOLO

onnx_model = YOLO("yolo11n.onnx")

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read() 
    results = onnx_model(frame)
    cv2.imshow("camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
