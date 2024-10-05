# pip install google.generativeai

import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY="xxxxxxxxxxxxxxxxxx" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)


## Upload PDF
sample_file1 = genai.upload_file(path="community_regulations.pdf", display_name="內政部公寓大廈管理條例")
print(f"Uploaded file '{sample_file1.display_name}' as: {sample_file1.uri}")

sample_file2 = genai.upload_file(path="community_rules.pdf", display_name="新竹椰城社區規約")
print(f"Uploaded file '{sample_file2.display_name}' as: {sample_file2.uri}")

## 驗證 PDF 檔案上傳及取得中繼資料
#file1 = genai.get_file(name=sample_file1.name)
#print(f"Retrieved file '{file1.display_name}' as: {sample_file1.uri}")

#file2 = genai.get_file(name=sample_file2.name)
#print(f"Retrieved file '{file2.display_name}' as: {sample_file2.uri}")


# Choose a Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# List all files
for file in genai.list_files():
    print(f"{file.display_name}, URI: {file.uri}")
    
## Prompting
#prompt = "根據所提供的文件, 請問區分所有權人會議每年需要召開一次嗎？"
prompt = "根據所提供的文件, 請問區分所有權人會議的召開通知, 開會前多久需要公告？"

response = model.generate_content([prompt, sample_file1, sample_file2])

print(response.text)
