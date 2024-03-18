## To run server: python llava_server.py
## To run client: python post_imgtxt.py

from PIL import Image
import requests

url = "http://127.0.0.1:5000/imgtxt/"

#prompt = "USER: <image>\nWhat are the things I should be cautious about when I visit this place?\nASSISTANT:"
#image = requests.get("https://llava-vl.github.io/static/images/view.jpg", stream=True).raw

#prompt = "USER: <image>\n這是什麼有名的台南美食?\nASSISTANT:"
#image = open("images/Tainan_BeefSoup.jpg", "rb")

prompt = "USER: <image>\n這是什麼著名的基隆景點?\nASSISTANT:"
image = open("images/daping_coast.jpg", "rb")

my_img = {'image': image }
my_txt = {'text' : prompt}

r = requests.post(url, files=my_img, data=my_txt)

print(r.text)
