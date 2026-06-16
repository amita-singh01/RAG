from services.rag_service import retrieve_documents


query = "My neighbour occupied my land"

results = retrieve_documents(
    query,
    "property"
)

for i, (doc, score) in enumerate(
    results,
    start=1
):
    print(f"\nResult {i}")
    print("-" * 50)
    print(f"Distance: {score}")
    print(doc.metadata)
    print(doc.page_content[:400])