from langchain_ollama import ChatOllama
from typing import TypedDict

base_url = "http:/localhost:11434"
model = "llama3.2"
temp = 0.5
num = 200

llm = ChatOllama(
    base_url=base_url,
    model = model,
    temperature=temp,
    num_predict=num
)

# Create Schema
class Review(TypedDict):
    summary : str
    sentiment  :str

structure_model = llm.with_structured_output(Review)


result = structure_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print("------------------------")
print(type(result))
print(result["summary"])
print(result["sentiment"])