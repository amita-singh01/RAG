from loaders.case_loader import (
    load_imported_cases,
    load_property_cases,
)

from services.document_service import build_documents
from services.chunking_service import chunk_documents
from services.embedding_service import SentenceTransformerEmbeddings
from services.faiss_service import build_and_save_index


def build_index():
    # Load data
    imported_cases = load_imported_cases()
    property_cases = load_property_cases()

    # Combine both datasets
    cases = imported_cases + property_cases

    print(f"Loaded {len(cases)} cases")

    # Convert to Documents
    documents = build_documents(cases)
    print(f"Created {len(documents)} documents")

    # Chunk Documents
    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")

    # Create Embedding Model
    embeddings = SentenceTransformerEmbeddings()

    # Build and Save FAISS Index
    build_and_save_index(chunks, embeddings)

    print("FAISS index created successfully!")


if __name__ == "__main__":
    build_index()