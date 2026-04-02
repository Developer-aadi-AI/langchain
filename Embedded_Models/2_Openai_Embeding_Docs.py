from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = "", dimensions=100)

docs = [
    "Delhi is capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is capital of France"
]

result = embeddings.embed_documents(docs)

print(str(result))

## This is used when you make RAG-Based applications