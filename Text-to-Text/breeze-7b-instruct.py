from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

#model_name = "MediaTek-Research/Breeze-7B-Base-v0.1"
model_name = "MediaTek-Research/Breeze-7B-Instruct-v0.1"

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "system", "content": "你是一個優秀資深的軟硬體設計工程師"},
    {"role": "user", "content": "我需要設計一個用微控制器製作的邊緣智慧裝置,請詳細介紹其應有的先進功能,並仔細介紹設計製作的細節?"}

#    {"role": "system", "content": "你是一個國內專業導遊"},
#    {"role": "user", "content": "我需要一個台南一日遊的行程,從早上午5點的六千牛肉湯開始安排, 傍晚要看到夕陽, 行程至晚上九點為止, 要逛到知名景點及吃到台南小吃美食,行程格式為 時間,景點名稱,地點住址,特色簡介 ,行程規劃很好的話,我會給你小費一千元作為獎勵"},
]

inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")

generated_ids = model.generate(inputs_ids, max_new_tokens=1000, pad_token_id=2)
response = tokenizer.batch_decode(generated_ids)[0]
print(response)

