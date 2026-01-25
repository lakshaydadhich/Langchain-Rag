import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableLambda,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()


def word_counter(text):
    return len(text.split())
prompt1=PromptTemplate(
    template="generate a joke on the given {topic}",
    input_variables=['topic']
)

chain1=RunnableSequence(prompt1|model|parser)
chain2=RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})
final_chain=chain1|chain2
result=final_chain.invoke("AI")
print(result)

