# pip install gpt4all
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
prompt = "why is the sky blue?"
output = model.generate(prompt, max_tokens=512)
print(output)
