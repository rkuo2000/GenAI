# pip install google-genai
# usage: python gemini_img2csv.py 113-07-1.jpg
import sys
from google import genai
import PIL.Image
import os

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

## for 存摺影本
filename = sys.argv[1] # with ext
img = PIL.Image.open(filename)

prompt = "根據這張圖片,按年月日,摘要,支出, 存入, 結存, 備註, 產生csv表格,並去掉數值的逗點"

response = client.models.generate_content(
   model="gemini-3-flash-preview",
   contents= [prompt , img]
)
print(response.text)

name_and_ext = os.path.splitext(filename)
file_name = name_and_ext[0]

with open(file_name+'.csv', 'w') as f:
    f.write(response.text)
