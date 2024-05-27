## To run server: python llava_server.py
## To run client: python post_imgtxt.py img_path/file.jpg

import sys
import requests

url = "http://127.0.0.1:5000/imgtxt/"

if len(sys.argv) < 2:
    image = requests.get("https://llava-vl.github.io/static/images/view.jpg", stream=True).raw
else:
    filename = sys.argv[1]
    image = open(filename, "rb")

#prompt = "USER: <image>\nWhat are the things I should be cautious about when I visit this place?\nASSISTANT:"
#prompt = "USER: <image>\n這是什麼?\nASSISTANT:"
#prompt = "USER: <image>\n這是我家的什麼場所?\nASSISTANT:"
#prompt = "USER: <image>\nWhat is this place?\nASSISTANT:"
prompt = "What is the place in my home?"
#prompt = "這是我家的什麼場所?"

my_img = {'image': image }
my_txt = {'text' : prompt}

r = requests.post(url, files=my_img, data=my_txt)

print(r.text)
