import os
from mistralai import Mistral

API_KEY = os.environ["MISTRAL_API_KEY"]
model_id = "magistral-medium-latest"

client = Mistral(api_key=API_KEY)

r = client.chat.complete(
    model = model_id,
    messages = [
        {
            "role": "user",
            "content": "John is one of 4 children. The first sister is 4 years old. Next year, the second sister will be twice as old as the first sister. The third sister is two years older than the second sister. The third sister is half the age of her older brother. How old is John?",
        },
    ],
    # prompt_mode = "reasoning" if you want to explicitly use the default system prompt, or None if you want to opt out of the default system prompt.
)

print(r.choices[0].message.content)
