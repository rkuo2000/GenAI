import ollama

prompt = 'Why is the sky blue? please answer briefly.'

response = ollama.chat(
    model='gemma3',
    messages=[ { 'role': 'user', 'content': prompt, } ]
)

print(response['message']['content'])
