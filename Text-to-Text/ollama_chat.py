import ollama

prompt = 'Why is the sky blue?'

response = ollama.chat(
#    model='snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0', # TAIDE
#    model='llama3.1',
    model='tinyllama',
#    model='gemma2:2b',
    messages=[ { 'role': 'user', 'content': prompt, } ]
)

print(response['message']['content'])
