import ollama

res = ollama.chat(
    model="llama3.2-vision",
    messages=[
        {"role": "user", "content": "Describe the image", "images": ["./images/taxi.jpg"]}
    ],
)

print(res['message']['content'])
