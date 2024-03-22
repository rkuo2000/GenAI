## Import Packages
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

## Load Model
model_name="meta-llama/Llama-2-7b-chat-hf"

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

## Assign system's role & your prompt

role = "Human Companion"
prompt = "how are you"

#role = "你是一個優秀資深的軟硬體設計工程師"
#prompt = "我需要設計一個用微控制器製作的邊緣智慧裝置,請詳細介紹其應有的先進功能,並仔細介紹設計製作的細節?"

#role = "你是一個專業導遊"
#prompt = "我需要一個台南一日遊的行程,從早上午5點的六千牛肉湯開始安排, 傍晚要看到夕陽, 行程至晚上九點為止, 行程格式為 時間,景點名稱,地點住址,特色簡介,這個行程對我很重要,如果規劃很好的話,我會給你小費一千元作為獎勵"

#role = "你是一位當過直轄市市長的人"
#prompt = "你將被總統任用為行政院長,請列舉你未來一年的施政方針,與闡明施政的內容,解釋其對國家與人民的重要性,並仔細介紹可行的實施辦法, 這對全體國民很重要,如果你的說明讓我很滿意,我會支持你繼續擔任該職務,並經常給你按讚關注"

#role = "你是一個人形機器人"
#prompt = "我需要你去煮一杯咖啡給我喝,請列出你要做的步驟,並仔細說明你需要做出的動作"

messages = [ 
    {"role": "system", "content": role}, 
    {"role": "user", "content": prompt}
]

## Apply template & Generate output
inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
generated_ids = model.generate(inputs_ids, max_new_tokens=1024, pad_token_id=2)

## Decode output & Print
output= tokenizer.batch_decode(generated_ids)[0]
textout = output.split("[/INST]")[-1]
print(textout)

