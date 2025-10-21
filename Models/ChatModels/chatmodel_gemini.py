from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

user_query = input("Describe your symptoms: ")

prompt = f"""
You are a health assistant, not a doctor.
When users describe their symptoms, you should:
- Provide general health information only.
- Never prescribe medicines or make a diagnosis.
- Always advise seeing a doctor if symptoms persist or worsen.

User: {user_query}
"""

result = model.invoke(prompt)
print("\nAI Health Assistant:\n", result.content)





