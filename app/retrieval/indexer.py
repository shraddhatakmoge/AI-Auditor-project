from app.retrieval.loader import load_documents
from app.retrieval.splitter import split_documents
from app.retrieval.vector_store import get_pinecone_index


NAMESPACE = "ai-auditor"


def index_documents():

    documents = load_documents(
        "data/raw/laptop_evidence.txt"
    )

    chunks = split_documents(documents)

    index = get_pinecone_index()

    records = []

    for i, chunk in enumerate(chunks):

        records.append(
            {
                "_id": f"laptop-{i}",
                "text": chunk.page_content
            }
        )

    index.upsert_records(
        namespace=NAMESPACE,
        records=records
    )

    print(f"Indexed {len(records)} documents.")


if __name__ == "__main__":
    index_documents()