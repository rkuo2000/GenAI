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

#prompt = "What are the things I should be cautious about when I visit this place?"
prompt = "What is this ?"
#prompt = "What is this place?"
#prompt = "What is the place in my house?"
#prompt = "這是什麼?"
#prompt = "這是我家的什麼場所?"

my_img = {'image': image }
my_txt = {'text' : prompt}

r = requests.post(url, files=my_img, data=my_txt)

print(r.text)
