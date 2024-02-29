import requests

url = "http://xxx"

# just set files to a list of tuples of (form_field_name, file_info)
multiple_files = [
        ('images', ('xxx.jpeg', open('xxx.jpeg', 'rb'), 'image/png')),
        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))
]

text_data = {"key":"value"}
headers = {
    "Authorization" : "xxx",
    "Content-Type": "application/json"
}
r = requests.post(url, files=multiple_files, data=text_data, headers=headers)
r.text
