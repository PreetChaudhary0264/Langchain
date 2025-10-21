from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generator'
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='write a summary for the following poem {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = PyPDFLoader('Community_Health_Watch_Solution.pdf')
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
