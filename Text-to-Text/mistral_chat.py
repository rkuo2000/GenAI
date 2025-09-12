# pip install mistralai

import os
from mistralai import Mistral

API_KEY = os.environ["MISTRAL_API_KEY"] # https://console.mistral.ai/api-keys

#model_id = "mistral-large-latest"
#model_id = "mistral-medium-latest"
model_id = "magistral-small-latest"

client = Mistral(api_key=API_KEY)

r = client.chat.complete(
    model = model_id,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

print(r.choices[0].message.content)
