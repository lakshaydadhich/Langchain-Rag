import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variable=['topic']
)
prompt2=PromptTemplate(
    template="Explain the given {topic}",
    input_variable=['topic']
)
parser=StrOutputParser()

joke_generator_chain=RunnableSequence(prompt1|model|parser)
result=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2|model|parser)
})

final_chain=RunnableSequence(joke_generator_chain,result)
answer=final_chain.invoke({'topic':'AI'})
print(answer)

