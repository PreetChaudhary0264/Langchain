from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='dummy.csv')
docs = loader.load()

print(docs[0])