import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=ChatGoogleGenerativeAI(model="models/gemini-2.5-flash",temperature=0)
template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Write a 5 line ' \
    'summary on the following text /n {text}',
    input_variables=['text']
)

prompt1=template1.format('black hole')

result=model.invoke(prompt1)

prompt2=template2.format({result.content})

result1=model.invoke(prompt2)

print(result1.content)


