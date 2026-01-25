import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BasrModel,Field
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=ChatGoogleGenerativeAI(model="models/gemini-2.5-flash",temperature=0)

class Person(BaseModel):
    name:str=Field(description="Name of the person")
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description="Name of the city where person live")

parser=PydanticOutputParser(pydantic_object=Person)

PromptTemplate(
    template='Generate the name,age and city of a fictional {place} persom\n'{format_instruction},
    input_variables=['places'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template|model|parser
result=chain.invoke({'bikaner'})
print(result)