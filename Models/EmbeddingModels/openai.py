from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
#jab ek query deni ho
result = embedding.embed_query("Delhi is the capital of india")

documents = [
    "Delhi is the capital of india",
    "Kolkata is the capital of india",
    "Mumbai is the capital of india"
]

#jab bhot sari queries ek sath deni ho
result = embedding.embed_documents(documents)
#vector ko string me convert kr liya
print(str(result)) 
