from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

base_url = "http://localhost:11434"
model = "llama3.2"

messages = [SystemMessage("You are a helpful AI assistant")]

llm = ChatOllama(
    base_url=base_url,
    model=model,
    temperature=0.9,
    num_predict=100
)

while True:
    prompt = input("User : ")
    if prompt.lower() == "exit":
        break
    messages.append(HumanMessage(prompt))
    result = llm.invoke(messages)
    content = result.content
    messages.append(AIMessage(content))
    print("AI : ", content)
