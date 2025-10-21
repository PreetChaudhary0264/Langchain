from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='projectsFolder',
    glob='*.pdf',
    loader_cls=PyPDFLoader
    #pehla parameter folder ka path => 2nd parameter konsi files extract krni hai => 3rd parameter konsa loader use kr rhe ho(hmari saari pdf files hai isliye pyPDFLoader)
)

docs = loader.load()

print(len(docs))
print(docs[9 ].page_content)

# docs = loader.lazy_load()
# for document in docs:
#     print(document.metadata) 
