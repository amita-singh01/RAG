# test_load.py

from services.embedding_service import SentenceTransformerEmbeddings
from services.faiss_service import load_index

embeddings = SentenceTransformerEmbeddings()

print("Before loading")

store = load_index(
    embeddings,
    "property"
)

print("After loading")