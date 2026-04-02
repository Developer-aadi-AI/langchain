from langchain_openai import OpenAI # This is an itegration package which tells langchain how to talk with OpenAI Api
# OpenAI is used for LLMs
from dotenv import load_dotenv  # dotenv is responsible for loading api key from .env file

load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

result = llm.invoke("What is the Capital of india?") # Invoke is used to communicate with particular model
print(result)

## Note: LLMs are very old technologies and nobody uses LLMs any more so we will not further work on this 