import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()
prompt1=PromptTemplate(
    template="Generate a tweet about a {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Generate a LinkedIn Post about the given {topic}",
    input_variable=['topic']
)
chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1|model|parser),
    'linked_post':RunnableSequence(prompt2|model|parser)
})
result=chain.invoke({'topic':'AI'})
print(result)