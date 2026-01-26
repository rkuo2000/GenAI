import os
from mistralai import Mistral

API_KEY = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=API_KEY)

model_id = "codestral-latest"
prompt = "def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():"

r = client.fim.complete(model=model_id, prompt=prompt, temperature=0)

print(
    f"""
{prompt}
{r.choices[0].message.content}
"""
)
