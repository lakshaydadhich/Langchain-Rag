from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
template1=PromptTemplate(
    template="provide a detailed report on {topic}",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="provide a 5 pointer summary of text on {text}",
    input_variables=['topic']
)
parser=StrOutputParser()
chain1=template1|model|parser|template2|model|parser
result1=chain1.invoke({'topic':'AI'})
print(result1)

