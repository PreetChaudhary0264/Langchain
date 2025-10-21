from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

# def wordCount(text):
#     return len(text.split())

prompt1 = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)
model = GoogleGenerativeAI(model='gemini-2.5-pro')
parser = StrOutputParser()

seq_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'No.of words':RunnableLambda(lambda x: len(x.split()))
})
final_chain = RunnableSequence(seq_chain,parallel_chain)
result = final_chain.invoke({'topic':'AI'})
print(result) 