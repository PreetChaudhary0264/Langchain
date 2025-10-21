from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
     Artificial Intelligence (AI) has rapidly evolved over the past decade, transforming industries and redefining the boundaries of what machines can do. From self-driving cars to
     language models capable of understanding and generating human-like text, AI has become a core component of modern technology. However, as AI continues to advance, it also raises
     ethical and societal concerns. Questions about data privacy, algorithmic bias, and the future of employment are now at the forefront of public discussions. To ensure AI benefits
     humanity as a whole, collaboration between researchers, policymakers, and the general public is essential.
 
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)
 
result = splitter.split_text(text)
print(len(result))
print(result)