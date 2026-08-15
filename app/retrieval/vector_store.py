from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(documents):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    return vector_store