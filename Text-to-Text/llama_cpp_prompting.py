# pip install llama-cpp-python
# pip install huggingface-hub

#from huggingface_hub import login
#login()

from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_name = "taide/Llama3-TAIDE-LX-8B-Chat-Alpha1-4bit" # TAIDE
model_file = "taide-8b-a.3-q4_k_m.gguf"

model_path = hf_hub_download(model_name, filename=model_file)
print(model_file)

LLM = Llama(model_path=model_path, n_ctx=16000, n_threads=32, n_gpu_layers=0)

prompt = "Hello, How are you?"

outputs = LLM(prompt, 
      max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
)
out_text=outputs["choices"][0]["text"]
print(out_text)
