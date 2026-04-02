from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs = [
    "Delhi is capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is capital of France"
]


embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")

vector = embeddings.embed_documents(docs)

print(str(vector))