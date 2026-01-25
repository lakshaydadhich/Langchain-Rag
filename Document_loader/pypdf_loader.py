from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(r"C:\Users\Lakshay\OneDrive\Desktop\langchains\RAG\dl-curriculum.pdf")
docs=loader.load()
print(docs[0].page_content)