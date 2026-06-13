from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Neighbour occupied my land",
    "Property encroachment dispute",
    "Domestic violence complaint"
]

embeddings = model.encode(sentences)

print("Number of vectors:", len(embeddings))
print("Dimension of first vector:", len(embeddings[0]))
print("First 10 values:")
print(embeddings[0][:10])