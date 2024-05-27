## To run server: python llava_server.py
## To run client: python post_imgtxt.py img_path/file.jpg

import sys
import requests

filename = sys.argv[1]
url = "http://127.0.0.1:5000/imgtxt/"

#prompt = "USER: <image>\nWhat are the things I should be cautious about when I visit this place?\nASSISTANT:"
#image = requests.get("https://llava-vl.github.io/static/images/view.jpg", stream=True).raw

#prompt = "USER: <image>\n這是什麼?\nASSISTANT:"
#prompt = "USER: <image>\n這是我家的什麼場所?\nASSISTANT:"
#prompt = "USER: <image>\nWhat is this place?\nASSISTANT:"
prompt = "USER: <image>\nWhat is the place in my home?\nASSISTANT:"

image = open(filename, "rb")

my_img = {'image': image }
my_txt = {'text' : prompt}

r = requests.post(url, files=my_img, data=my_txt)

print(r.text)
