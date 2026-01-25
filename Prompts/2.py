import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("models/gemini-2.5-flash")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.header("Research Tool")
paper_input=st.selectbox("choose paper input",["Attention All You Need","Gitinjali","AI"])
style_input=st.selectbox("choose Explaination style input",["one simple paragraph","Bullet Points","two paragraph"])
length_input=st.selectbox("select length input",["Short (1-2 paragraphs)","Medium (3-5 paragraph)","Long (detailed explaination)"])


template=PromptTemplate(
    template="""
Please simmarixe the research paper titled "{paper_input}" with the following specification:
Explaination Style:{style_input}
Explaination Length:{length_input}
""",
input_variables=['paper_input','style_input','length_input'],
validate_template=True
)
prompt=template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)


if st.button("Submit"):
    result=get_gemini_response(prompt)
    st.write(result)