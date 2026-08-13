from app.retrieval.loader import load_documents
from app.retrieval.splitter import split_documents
from app.retrieval.vector_store import create_vector_store


def create_retriever():

    documents = load_documents(
        "data/raw/laptop_evidence.txt"
    )

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    return vector_store.as_retriever(
        search_kwargs={
            "k": 3
        }
    )