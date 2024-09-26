import requests
import torch
from PIL import Image
from transformers import pipeline

#model_id = "meta-llama/Llama-3.2-1B-Instruct"
model_id = "meta-llama/Llama-3.2-3B-Instruct"

pipe = pipeline( "text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto",)

role = "你是一個優秀資深的軟硬體設計工程師"
prompt = "我需要設計一個用微控制器製作的邊緣智慧裝置,請詳細介紹其應有的先進功能,並仔細介紹設計製作的細節?"

#role = "你是一個專業導遊"
#prompt = "我需要一個台南一日遊的行程,從早上午5點開始安排, 傍晚要看到夕陽, 行程至晚上九點為止, 行程格式為 時>間,景點名稱,地點住址,特色簡介,這個行程對我很重要,如果規劃很好的話,我會給你小費一千元作為獎勵"

#role = "你是一位當過直轄市市長的人"
#prompt = "你將被總統任用為行政院長,請列舉你未來一年的施政方針,與闡明施政的內容,解釋其對國家與人民的重要性,並仔細介紹可行的實施辦法, 這對全體國民很重要,如果你的說明讓我很滿意,我會支持你繼續擔任該職務,並經常給你按讚關注"

#role = "你是一個人形機器人"
#prompt = "我需要你去煮一杯咖啡給我喝,請列出你要做的步驟,並仔細說明你需要做出的動作"

messages = [
    {"role": "system", "content": role},
    {"role": "user", "content": prompt}
]

outputs = pipe(messages, max_new_tokens=512)
print(outputs[0]["generated_text"][-1]["content"])

