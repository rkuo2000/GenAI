# pip install pyreft

import torch, transformers
from pyreft import (
    ReftModel,
    get_intervention_locations
)

prompt_no_input_template = """Below is an instruction that \
describes a task. Write a response that appropriately \
completes the request.

### Instruction:
%s

### Response:
"""

device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "meta-llama/Llama-2-7b-hf"

reft_model_name = "zhengxuanzenwu/Loreft1k-Llama-2-7b-hf"

tokenizer = transformers.AutoTokenizer.from_pretrained(model_name, model_max_length=2048, padding_side="right", use_fast=False)
tokenizer.pad_token = tokenizer.unk_token

model = transformers.AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map=device)

reft_model = ReftModel.load( reft_model_name, model, from_huggingface_hub=True)
reft_model.set_device(device)


instruction = "Tell me about the NLP Group at Stanford University."

# tokenize and prepare the input
prompt = prompt_no_input_template % instruction
prompt = tokenizer(prompt, return_tensors="pt").to(device)

intervention_locations = torch.tensor([get_intervention_locations(
    last_position=prompt["input_ids"].shape[-1], positions="f5+l5",
    num_interventions=len(reft_model.interventions))]).permute(1, 0, 2).tolist()

# generate
_, reft_response = reft_model.generate(
    prompt, 
    unit_locations={"sources->base": (None, intervention_locations)},
    intervene_on_prompt=True, max_new_tokens=512, do_sample=False, 
    no_repeat_ngram_size=5, repetition_penalty=1.1,
    eos_token_id=tokenizer.eos_token_id, early_stopping=True
)

textout = tokenizer.decode(reft_response[0], skip_special_tokens=True)
print(textout)

