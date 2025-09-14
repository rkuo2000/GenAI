
# pip install --upgrade huggingface_hub
# pip install smolagents[toolkit]

import os
HF_TOKEN=os.environ.get("HF_ACCESS_TOKEN")

from huggingface_hub import login
login(token=HF_TOKEN)

from smolagents import CodeAgent, InferenceClientModel

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel()  # Uses a default model

# Create an agent with no tools
agent = CodeAgent(tools=[], model=model)

# Run the agent with a task
result = agent.run("Calculate the sum of numbers from 1 to 10")
print(result)
