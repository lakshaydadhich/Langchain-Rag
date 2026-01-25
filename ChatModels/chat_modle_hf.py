from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id="",
    task=""
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("who is king of cricket")
print(result.content)