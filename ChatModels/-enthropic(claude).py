from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
model=ChatAnthropic()
result=model.invoke("who is run machine?")
print(result.content)