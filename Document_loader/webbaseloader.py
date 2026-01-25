from langchain_community.document_loaders import WebBaseLoader
URL="https://en.wikipedia.org/wiki/Cricket"
loader=WebBaseLoader(URL)
docs=loader.load()
print(docs[0].page_content)