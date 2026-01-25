from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda

class Feedback(BaseModel):
    sentiment:Literal['Positive','negative']=Field(description='Give the sentiment of the feedback ')

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=Feedback)
prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive and negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
classify_chain=prompt1|model|parser2

prompt2=PromptTemplate(
    template='write an approptiate response to this positive feedback \n{feedback}',
    input_variable=['feedback']
)


prompt3=PromptTemplate(
    template='write an approptiate response to this negative feedback \n{feedback}',
    input_variable=['feedback']
)
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|model|parser),
    (lambda x:x.sentiment=='negative',prompt3|model|parser),
    RunnableLambda(lambda x: 'could not find sentiment')
    )


chain=classify_chain|branch_chain

response=chain.invoke({'feedback':'This is a terriable phone'})
print(response)

