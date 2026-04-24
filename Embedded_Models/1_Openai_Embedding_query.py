from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(models = 'text-embedding-3-small', dimensions=32)

result = embeddings.embed_query("What is the capital of India?")

print(str(result))



## This is used when you make RAG-Based applications


### Note: there are some more methods of encoding then vector encoding, some are:
#1 wordtovec
#2 Bert
#3 GloVe
#4 TF-IDF
#5 One-Hot encoding
#6 