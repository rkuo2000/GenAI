# pip install google.generativeai
# usage: python gemini_img2csv.py 113-07-1.jpg > 113-07-1.csv
import sys
import google.generativeai as genai
import PIL.Image
import os

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

## for 存摺影本
filename = sys.argv[1]

img = PIL.Image.open( filename)
prompt = "根據這張圖片,按年月日,摘要,支出, 存入, 結存, 備註, 產生csv表格,並去掉數值的逗點"
#prompt = "根據這張圖片,轉換成markdown格式的表格"

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content( [prompt , img] )
print(result.text)
