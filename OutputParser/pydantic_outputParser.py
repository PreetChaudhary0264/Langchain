from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)
 
model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description='name of the person')
    age:int =  Field(gt=18,description='age of the parson')
    city:str = Field(description='name of the city person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='generate name ,age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.format(place='indian')

#   print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)