from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

base_url = "http://localhost:11434"
model = "llama3.2"

messages = [SystemMessage("You are a helpfull AI assistant"),
            HumanMessage("Tell me about langchain in 2 lines")]

llm = ChatOllama(base_url=base_url,
                 model=model,
                 temperature=0.9,
                 num_predict=100)

result = llm.invoke(messages)

print(result.content)
messages.append(AIMessage(content = result.content))

print(messages)