from langchain_community.vectorstores import FAISS
from config.settings import FAISS_DIR


def build_and_save_index(chunks, embeddings):
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    FAISS_DIR.mkdir(parents=True, exist_ok=True)

    vector_store.save_local(str(FAISS_DIR))

    return vector_store