# pip install transformers accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

model_name = "yentinglin/Taiwan-LLM-7B-v2.0.1-chat"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print()

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
prompt =  "東北季風如何影響台灣氣候？"

messages = [
    {"role": "system", "content": "你是一個人工智慧助理",},
    {"role": "user",   "content": prompt},
]

inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")

generated_ids = model.generate(inputs_ids, max_new_tokens=256)

output= tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
textout = output.split("ASSISTANT: ")[-1]
print(textout)
