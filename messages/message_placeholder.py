from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

base_url = "http://localhost:11434"
model = "llama3.2"


chat_template = ChatPromptTemplate([('system','You are a helpful customer support agent'),
                                    MessagesPlaceholder(variable_name = 'chat_history'),
                                    ('human' , '{query}')])

chat_history = []
with open(file='C:/Users/bathr/Desktop/Cybrom_Class_Data/SELF GenAI Projects/Tutorial_files/LangChain/messages/history.txt') as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund?'})

llm = ChatOllama(
    base_url=base_url,
    model=model,
    temperature=0.9,
    num_predict = 200)

result = llm.invoke(prompt)

print(result.content)