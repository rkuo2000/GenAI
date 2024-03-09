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
]

inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")

generated_ids = model.generate(inputs_ids, max_new_tokens=1000, pad_token_id=2)
response = tokenizer.batch_decode(generated_ids)[0]
print(response)

