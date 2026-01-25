import os
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_key"))
model=ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")
parser=JsonOutputParser()
template=PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt=template.format()
# print(prompt)
# result=model.invoke(prompt)
# final=parser.parse(result.content)
# print(final)
# or
chain=template|model|parser
result=chain.invoke({'topic':'black hole'})
print(result)