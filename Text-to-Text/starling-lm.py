
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.set_default_device("cuda")

model_name = "Nexusflow/Starling-LM-7B-beta"
print(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="cuda")

def generate_response(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        max_length=256,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    response_ids = outputs[0]
    response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
    return response_text

# Single-turn conversation
prompt = "Hello, how are you?"
single_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant:"
response_text = generate_response(single_turn_prompt)
print("Response:", response_text)

## Multi-turn conversation
prompt = "Hello"
follow_up_question =  "How are you today?"
response = ""
multi_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant: {response}<|end_of_turn|>GPT4 Correct User: {follow_up_question}<|end_of_turn|>GPT4 Correct Assistant:"
response_text = generate_response(multi_turn_prompt)
print("Multi-turn conversation response:", response_text)

### Coding conversation
prompt = "Implement quicksort using C++"
coding_prompt = f"Code User: {prompt}<|end_of_turn|>Code Assistant:"
response = generate_response(coding_prompt)
print(response)

