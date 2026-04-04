from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

base_url = "http://localhost:11434"
model = "llama3.2"

chat_template = ChatPromptTemplate([('system', 'you are a helpful customer support agent'),
                                    MessagesPlaceholder(variable_name ='chat_history'),
                                    ('human', '{query}')]
                                    )

chat_history = []

with open(file = 'C:/Users/bathr/Desktop/Cybrom_Class_Data/SELF GenAI Projects/Tutorial_files/LangChain/ChatBots/history.txt') as f:
    chat_history.extend([line.strip() for line in f])

llm = ChatOllama(
    base_url=base_url,
    model=model,
    temperature=0.8,
    num_predict=220)

while True:
    query = input("user : ")
    if query.lower() == 'exit':
        break
    prompt = chat_template.invoke({'chat_history':chat_history,'query': query})
    result = llm.invoke(prompt)
    content = result.content
    print(content)
    chat_history.append(f"User : {query}")
    chat_history.append(f"AI : {content}")

with open('C:/Users/bathr/Desktop/Cybrom_Class_Data/SELF GenAI Projects/Tutorial_files/LangChain/ChatBots/history.txt', 'a') as f:
    f.write("\n".join(chat_history) + "\n")
    