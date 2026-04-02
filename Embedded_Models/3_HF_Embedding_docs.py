from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")

docs = [
    "Delhi is capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is capital of France"
]

vector = embedding.embed_documents(docs)

print(str(vector))