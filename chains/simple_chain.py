import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model=genai.GenerativeModel("models/gemini-2.5-flash")
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt=PromptTemplate(
    template="Generate 5 interesting fact about {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

chain=prompt|model|parser

result=chain.invoke({'topic':'AI'})
print(result)

chain.get_graph().print_ascii()