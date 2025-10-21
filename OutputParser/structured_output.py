from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)
 
model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact-1',description='Fact-1 about the topic'),
    ResponseSchema(name='fact-2',description='Fact-2 about the topic'),
    ResponseSchema(name='fact-3',description='Fact-3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give three facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.format(topic='blackhole')
result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)