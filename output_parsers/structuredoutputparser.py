import os
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_key"))
model=ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

schema=[
    ResponseSchema(name='fact_1',description='Fact 1 about topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about topic'),

]
parser=StructuredOutputSchema.from_response_schemas(schema)

template=PromptTemplate(
    template="Gives 3 fact about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({'topix':'black hole'})
result=model.invoke(prompt)
chain=template|model|parser
result=chain.invoke(prompt)