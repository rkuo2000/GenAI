import ollama

stream = ollama.chat(
#    model='snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0', # TAIDE
#    model='llama3.1',
#    model='tinyllama',
    model='gemma2:2b',
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
