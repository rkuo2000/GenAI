#!pip3 install transformers==4.47.0
#!pip3 install -U mtkresearch
#!pip3 install einops
from transformers import AutoModel, AutoTokenizer
from transformers import GenerationConfig
import torch
from mtkresearch.llm.prompt import MRPromptV3

model_id = 'MediaTek-Research/Llama-Breeze2-8B-Instruct-v0_1'
model = AutoModel.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True,
    device_map='auto',
    img_context_token_id=128212
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True, use_fast=False)

generation_config = GenerationConfig(
  max_new_tokens=2048,
  do_sample=True,
  temperature=0.01,
  top_p=0.01,
  repetition_penalty=1.1,
  eos_token_id=128009
)

prompt_engine = MRPromptV3()

sys_prompt = 'You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan.'

def _inference(tokenizer, model, generation_config, prompt, pixel_values=None):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    if pixel_values is None:
        output_tensors = model.generate(**inputs, generation_config=generation_config)
    else:
        output_tensors = model.generate(**inputs, generation_config=generation_config, pixel_values=pixel_values.to(model.dtype))
    output_str = tokenizer.decode(output_tensors[0])
    return output_str
conversations = [
    {"role": "system", "content": sys_prompt},
    {"role": "user", "content": [
        {
            "type": "image",
            "image_path": "images/test_big_data.png",
        },
        {
            "type": "text",
            "text": "請問前三名總共可獲得多少錢？"
        },
    ]},
]

prompt, pixel_values = prompt_engine.get_prompt(conversations)
output_str = _inference(tokenizer, model, generation_config, prompt, pixel_values=pixel_values)
result = prompt_engine.parse_generated_str(output_str)
print(result)
# {'role': 'assistant', 'content': '第一名可獲得30萬元，第二名可獲得20萬元，第三名可獲得15萬元。前三名總共可獲得65萬元。'}

