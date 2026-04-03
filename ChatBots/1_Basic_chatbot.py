from langchain_ollama import ChatOllama
from dotenv import load_dotenv


base_url = "http://localhost:11434"
model = "llama3.2"

llm = ChatOllama(
    base_url = base_url,
    model = model,
    temperature = 0.8,
    num_predict = 256
)

while True:
    prompt  = input("User : ")
    if prompt.lower() =='exit':
        break
    else:
        result = llm.invoke(prompt)
        print("AI : ", result.content)
        

