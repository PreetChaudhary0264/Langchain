from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/Philips-Battery-Powered-SkinProtect-Trimmer/dp/B0BXNVPRGS/ref=sr_1_1?adgrpid=1326012633048780&dib=eyJ2IjoiMSJ9.hLDX9Vvmznb528NEqEd5JghZKI4VLTfGolHhQ_aSYdxFZXiv9qqHSp926FqRDOeBDAshELAwce-pMGplTMFSuB-RrcMLcDZs923tECyUM2QfgKxdOGMZQ7e3fRYlKmEW1oy6hcnFLxnqU5zx9YRgrwm_ZQxOmBIe1LQwNsvzi_5YE__pEAUgLmJZX5LIZJZ6Bk9v3d89-SbnZVZ5zgp3FgtaeaiWdU-yELjuOo75lC0.uLxgdihrplT4OgI5A9rlyosdNLqPbU_-1ca4g3LUr_4&dib_tag=se&hvadid=82876055231412&hvbmt=be&hvdev=c&hvlocphy=150034&hvnetw=o&hvqmt=e&hvtargid=kwd-82876681051014%3Aloc-90&hydadcr=15412_2338239&keywords=flipkart&mcid=17b34daf6ece3007bf2f632e0be56074&msclkid=be7047ec24241ff93fc02f192d44c56b&qid=1760889186&sr=8-1"

loader = WebBaseLoader(url)
#ek url ke badle ek document mila .. yha list or URLs bhi bhej skte hai
docs = loader.load()

print(len(docs))
print(docs)