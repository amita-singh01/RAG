from services.embedding_service import SentenceTransformerEmbeddings
from services.faiss_service import load_index

embeddings = SentenceTransformerEmbeddings()

store = load_index(
    embeddings,
    "property"
)

print("Store loaded")

query = "My neighbour occupied my land"

print("Searching...")

results = store.similarity_search_with_score(
    query,
    k=5
)

print("\n--- Search Results ---")
for i, (doc, score) in enumerate(results, start=1):
    # Convert L2 distance to Cosine Similarity (assuming normalized embeddings)
    # Cosine Similarity = 1 - (L2_Distance^2) / 2
    cosine_sim = 1 - (score ** 2) / 2
    percentage = max(0, cosine_sim) * 100
    
    print(f"\nResult {i} | Similarity: {percentage:.2f}% (L2 Distance: {score:.4f})")
    print("-" * 50)
    print(f"Metadata: {doc.metadata}")
    print(f"Content Preview: {doc.page_content[:200]}...")

print("\nDone!")