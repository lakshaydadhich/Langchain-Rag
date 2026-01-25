from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro")
result=llm.invoke("who is king of cricket?")
print(result.content)