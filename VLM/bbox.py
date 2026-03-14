# Usage:
# python gemini_image.py images/recycle_bin.jpg
# edit bbox.json with the bbox of object detection
# python bbox.py images/recycle_bin.jpg

import cv2
import sys
import json

if len(sys.argv)>1:
    image = cv2.imread(sys.argv[1])
else:
    image = cv2.imread("images/recycle_bin.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

with open('bbox.json', 'r') as file:
    data = json.load(file)

color = (0,255,0) # RGB
thickness = 1

img = image

for d in data:
    pt1 = (d['bbox_2d'][0], d['bbox_2d'][1])
    pt2 = (d['bbox_2d'][2], d['bbox_2d'][3])
    img = cv2.rectangle(img, pt1, pt2, color, thickness)
    img = cv2.putText(img, d['label'], (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("objdet", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
