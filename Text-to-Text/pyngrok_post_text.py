## To run server: run pyngrok_LLM_Server.ipynb on Colab
## To run client: python pyngrok_post_text.py

import requests

# need to copy from the running pyngrok_LLM_Server.ipynb on Colab
url = "https://3780-34-126-65-43.ngrok-free.app/"
url = url+"text"

prompt = "How are you?"

r = requests.post(url, json={'text': prompt})

print(r.json())
