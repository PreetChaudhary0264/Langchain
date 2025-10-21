from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

model = GoogleGenerativeAI(model='gemini-2.5-pro')
parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)
result = chain.invoke({'topic':'AI'})
print(result) 
