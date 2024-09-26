import os
from mistralai import Mistral

#api_key = os.environ["MISTRAL_API_KEY"] # https://console.mistral.ai/api-keys
api_key = os.environ["JXUhRvC7bgBa5GOEQ9x8QSks2vB4a0li"]

model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

print(chat_response.choices[0].message.content)
