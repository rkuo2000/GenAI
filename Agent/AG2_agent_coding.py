# pip install ag2[gemini]

## To make a CONFIG_LIST
import os
API_KEY = os.environ.get("GEMINI_API_KEY")

## Agent coding
from autogen import AssistantAgent, UserProxyAgent, LLMConfig

llm_config = LLMConfig(
  api_type="google",
  model="gemini-2.5-flash",
  api_key=API_KEY
)

assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False})

user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task
