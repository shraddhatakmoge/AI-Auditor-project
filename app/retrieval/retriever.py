from langchain_core.runnables import RunnableLambda

from app.retrieval.loader import load_documents
from app.retrieval.splitter import split_documents
from app.retrieval.vector_store import create_vector_store


def create_retriever():

    documents = load_documents(
        "data/raw/laptop_evidence.txt"
    )

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    def retrieve(query):

        results = vector_store.similarity_search_with_relevance_scores(
            query,
            k=3
        )

        # Only keep genuinely relevant evidence
        relevant_documents = [
            document
            for document, score in results
            if score >= 0.50
        ]

        return relevant_documents

    return RunnableLambda(retrieve)