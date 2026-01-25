from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="",
    glob='*.pdf',
    loader_cls="pypdf"
)
docs=loader.load()
print(docs[0])