from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0.4,max_completion_tokens=100)
result = model.invoke("What is the capital of india")
print(result)
print(result.content)

