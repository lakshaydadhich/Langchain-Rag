from langchain_community.document_loaders import CSVLoader
csv_path=r"C:\Users\Lakshay\OneDrive\Desktop\langchains\RAG\Social_Network_Ads (1).csv"
loader=CSVLoader(csv_path)
docs=loader.load()
print(docs[0])