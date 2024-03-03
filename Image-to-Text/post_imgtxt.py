import requests

url = "http://127.0.0.1:8000"

# just set files to a list of tuples of (form_field_name, file_info)
image_files = [ ('images', ('NTOU_frontgate.jpg', open('images/NTOU_frontgate.jpg', 'rb'), 'image/jpg')),
]

#prompt = {"USER: <image>\nDo you know who that is?\nASSISTANT:"}
prompt = {"key":"value"}
headers = {
    "Authorization" : "xxx",
    "Content-Type": "application/json"
}

r = requests.post(url, files=image_files, data=prompt, headers=headers)
print(r.text)
