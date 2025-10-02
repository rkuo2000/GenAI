#!/home/user/venv/bin/python

import os
import cv2
import time
from PIL import Image
from ultralytics import YOLO

#onnx_model = YOLO("yolo11n.onnx")
model = YOLO("tank_best.pt")

cap = cv2.VideoCapture(0)

prev_frame_time = 0

while (cap.isOpened()):
    ret, frame = cap.read() 
    new_frame_time = time.time()

    results = model(frame)
    annotated_image = results[0].plot() #

    if (new_frame_time - prev_frame_time)> 0:
        fps = 1/ (new_frame_time - prev_frame_time)
    else:
        fps = 0

    prev_frame_time = new_frame_time
    fps_text = f"FPS: {int(fps)}"

    cv2.putText(annotated_image, fps_text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow("YOLO11", annotated_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
