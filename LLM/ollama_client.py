import ollama

prompt = 'Why is the sky blue? please answer briefly.'

response = ollama.chat(
    model='gemma4-e2b',
    messages=[ { 'role': 'user', 'content': prompt, } ]
)

print(response['message']['content'])
