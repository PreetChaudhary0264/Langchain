from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = GoogleGenerativeAI(model='gemini-2.5-pro')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description='Give the sentiment of the feedback'),
    feedback: str = Field(description='Feedback provided by the user')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n{feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

# classifier_chain = prompt1 | model | parser
#guarrentee nhi hai ki yee LLM positive ya negative hi result de kya pta result kuch aisa de=> This is a positive statement(ya fir kuch orr)
#isliye hme output ko structure krn pdega isliye we are using pydantic output parser

classifier_chain = prompt1 | model | parser2 | RunnableLambda(lambda x: x.dict())

# result = classifier_chain.invoke({'feedback':"This is a wonderful smartphone"}).sentiment

prompt2 = PromptTemplate(
    template='Write an appropriate 5 lines response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x['sentiment'] == 'positive' , prompt2 | model | parser),
    (lambda x:x['sentiment'] == 'negative' , prompt3 | model | parser),
    RunnableLambda(lambda x:"Could not find Sentiment")
)

final_chain = classifier_chain | branch_chain
result = final_chain.invoke({'feedback': 'This is a beautiful phone'})
print(result)

