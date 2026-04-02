from langchain_openai import ChatOpenAI # ChatOpenAI is used for chat models
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4") ## 1. You can also provide temperature parameter for creativity.
# some imp values of temperature
# Factual Answers (Math, code, Facts)                  0.0 to 0.3
# Balanced Response (General QA, Explanations)         0.5 to 0.7
# Creative writing, Storytelling, Jokes                0.9 to 1.2
# Maximum Randomness (wild ideas, Brainstorming)       1.5+

## 2. And max_completion_token parameter for How many tokens long your output should be.

result = model.invoke("What is the Capital of India?")

print(result)  # This gives answers with metadata
# To print the actual output we use 
print(result.content)