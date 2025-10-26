from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# --- Use API-based Embeddings (No Local Model Download) ---
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

# --- Documents ---
doc1 = Document(
    page_content="Virat Kohli is one of the most celebrated batsmen in modern cricket. Known for his aggressive batting style and fierce competitiveness, he has broken numerous records across all formats. Kohli’s consistency, passion for the game, and leadership skills have made him a role model for aspiring cricketers worldwide.",
)

doc2 = Document(
    page_content="Rohit Sharma, also called the Hitman, is famous for his ability to score big hundreds, especially in limited-overs cricket. With elegant stroke play and incredible timing, he holds multiple records for the highest individual scores in ODIs. His calm leadership style as captain has also led India to major victories.",
)

doc3 = Document(
    page_content="MS Dhoni, often referred to as 'Captain Cool', is legendary for his calm demeanor under pressure and sharp cricketing brain. An exceptional wicketkeeper-batsman, he led India to win the ICC T20 World Cup (2007), ICC ODI World Cup (2011), and ICC Champions Trophy (2013). Dhoni is revered for finishing matches with calm authority and strategic brilliance.",
)

doc4 = Document(
    page_content="Jasprit Bumrah is one of the most lethal fast bowlers in world cricket today. Known for his unique bowling action, deadly yorkers, and precise control, he has become India’s go-to bowler in all formats. Bumrah’s ability to deliver under pressure — especially in the death overs — makes him one of the finest match-winners of modern cricket. Despite his calm personality, his fiery spells have dismantled the best batting lineups around the world.",
)
doc5 = Document(
    page_content="Langchain is used to build LLM based applications"
)
doc6 = Document(
    page_content="Langchain make it easy to work with LLMs"
)
doc7 = Document(
    page_content="Langchain supports chroma,Faiss"
)

# --- Add all documents ---
docs = [doc1, doc2, doc3, doc4,doc5,doc6,doc7]


# --- Chroma Vector Store ---
vector_store = Chroma(
    embedding_function=embeddings,
    collection_name="example",
    persist_directory="./chroma_langchain_db"
)
ids = vector_store.add_documents(documents=docs)

retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k":2,"lambda_mult":0.5 })

query = "what is langchain"
result = retriever.invoke(query)


for i,doc in enumerate(result):
    print(f"\n---Result{i+1} ---")
    print(f"Content:\n{doc.page_content}...")