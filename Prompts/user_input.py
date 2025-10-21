from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research tool")
# user_input = st.text_input("Enter your prompt")
paper_input = st.selectbox("Select research paper name",["Attention is all u need","Diffusion models beat gans on image synthesis"])
style_input = st.selectbox("Select Explanation style",["Beginner-friendly","Technical"])
length_input = st.selectbox("Select Explanation length",["Short","Medium","Long"])

template = PromptTemplate(
    input_variables=['paper_input','style_input','length_input'],
    validate_template=True,
    template="""
      Please summarize the research peper titled {paper_input} with the following specification:
      explanation style:{style_input}
      explanation length:{length_input}
      1.Mathematical details:
        -include relevant mathematical details if present in the paper
      2. Analogies:
        use relatable analogies to simplify complex ideas
    
    """
)

# template = load_prompt('template.json')

prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)


model = GoogleGenerativeAI(model='gemini-2.5-pro')

if st.button('Summarize'):
    if not prompt.strip():
        st.warning("PLease enter some text")
    else:
        with st.spinner("Summarazing..."):
            result = model.invoke(prompt)
            st.write(result)
        