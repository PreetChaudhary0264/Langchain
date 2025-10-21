from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name,age,city of a fictional person. \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
#ye input variable isliye nhi hai bcoz hum user se runtim eprr nhi lere ye runtime se pehle hi fill ho jayga

# prompt = template.format()
# # print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

#using chains

chain = template | model | parser

final_result = chain.invoke({})
#invoke function always expect an input thats why empty dictionary is given here
print(final_result)
