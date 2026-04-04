from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

base_url = "http://localhost:11434"
model = "llama3.2"


chat_template = ChatPromptTemplate([('system','you are a helpful {domain} expert'),
                                    ('human' , 'Explain this in simple terms, What is {topic}')])

prompt  = chat_template.invoke({'domain':'Machine Learning', 'topic':'Artificial Intelligence'})

llm = ChatOllama(
    base_url=base_url,
    model = model,
    temperature=0.9,
    num_predict=100
)

result = llm.invoke(prompt)
print(result.content)