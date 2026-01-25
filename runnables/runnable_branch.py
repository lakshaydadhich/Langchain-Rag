import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableLambda,RunnablePassthrough,RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate a report about {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)    
chain1=RunnableSequence(prompt1,model,parser)

chain2 = RunnableBranch(
    (
        lambda x: len(x.split()) > 500,
        RunnableSequence(prompt2 | model | parser)
    ),
    RunnablePassthrough()
)
final_chain=RunnableSequence(chain1,chain2)
result=final_chain.invoke({'topic':'russia vs ukraine'})
print(result)