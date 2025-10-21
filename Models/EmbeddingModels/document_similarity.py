# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat kohli is a aggressive batter",
    "Rohit sharma is aggresive when needed",
    "Ms Dhoni is cool captain",
    "Kl Rahul is a classy batsman. An all position player"
]

query = 'Tell me about kl rahul' 

documentEmbedding = embedding.embed_documents(documents)
queryEmbedding = embedding.embed_query(query)

# print(cosine_similarity([queryEmbedding],documentEmbedding))
scores = cosine_similarity([queryEmbedding],documentEmbedding)[0]

index,score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(documents[index])
print("Similarity Score is",score)