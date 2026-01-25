import os
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai 
from dotenv import load_dotenv
from typing import TypedDict,Annotated
load_dotenv()
model=ChatGoogleGenerativeAI(model="models/gemini-2.5-flash",temperature=0)

class Review(TypedDict):
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return sentiment of review"]

structured_model=model.with_structured_output(schema=Review, include_raw=False )
result=structured_model.invoke("""The hardware is great,but the software feels bloated.There are too many pre-installed apps that I can't remove. Also,the UI looks outdated compared to other brands.Hoping for a software update to fix this.""")

print(result)
print(result['summary'])
print(result['sentiment'])