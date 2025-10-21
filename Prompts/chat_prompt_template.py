from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage,HumanMessage

chat_template = ChatPromptTemplate([
    ('system','You are a {domain} expert'),
    ('human','Explain in simple terms, what is {topic}'),
    # SystemMessage(content='You are a {domain} expert') but it will not work
])

prompt = chat_template.invoke({'domain':'cricket','topic':'dusra'})
print(prompt)