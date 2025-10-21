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
    metadata={"team": "Royal Challengers Bangalore"}
)

doc2 = Document(
    page_content="Rohit Sharma, also called the Hitman, is famous for his ability to score big hundreds, especially in limited-overs cricket. With elegant stroke play and incredible timing, he holds multiple records for the highest individual scores in ODIs. His calm leadership style as captain has also led India to major victories.",
    metadata={"team": "Mumbai Indians"}
)

doc3 = Document(
    page_content="MS Dhoni, often referred to as 'Captain Cool', is legendary for his calm demeanor under pressure and sharp cricketing brain. An exceptional wicketkeeper-batsman, he led India to win the ICC T20 World Cup (2007), ICC ODI World Cup (2011), and ICC Champions Trophy (2013). Dhoni is revered for finishing matches with calm authority and strategic brilliance.",
    metadata={"team": "Chennai Super Kings"}
)

doc4 = Document(
    page_content="Jasprit Bumrah is one of the most lethal fast bowlers in world cricket today. Known for his unique bowling action, deadly yorkers, and precise control, he has become India’s go-to bowler in all formats. Bumrah’s ability to deliver under pressure — especially in the death overs — makes him one of the finest match-winners of modern cricket. Despite his calm personality, his fiery spells have dismantled the best batting lineups around the world.",
    metadata={"team": "Mumbai Indians"}
)

# --- Add all documents ---
docs = [doc1, doc2, doc3, doc4]

# --- Chroma Vector Store ---
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory='./chroma_db',
    collection_name='sample'
)

# --- Store documents and get their IDs ---
ids = vector_store.add_documents(documents=docs)

# --- Queries ---
print("\nSimilarity Search:")
print(vector_store.similarity_search(query="who among these are an opener", k=1))

print("\nSimilarity Search With Score:")
print(vector_store.similarity_search_with_score(query="who among these are an opener", k=1))

print("\nFiltered Search (team = Mumbai Indians):")
print(vector_store.similarity_search_with_score(
    query="who among these are an opener",
    filter={'team': 'Mumbai Indians'}
))

# --- Update a document ---
updated_doc = Document(
    page_content="This is updated",
    metadata={'team': "RCB"}
)
vector_store.update_document(document_id=ids[0], document=updated_doc)
print("\nDocument updated successfully.")