from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

doc=PyPDFLoader(r'C:\Users\Lakshay\OneDrive\Desktop\langchains\RAG\dl-curriculum.pdf')

docs=doc.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_documents(docs)
#print(result)
print(result[0])
