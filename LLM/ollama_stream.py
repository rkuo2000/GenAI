import ollama

prompt = "Why is the sky blue?"

stream = ollama.chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
