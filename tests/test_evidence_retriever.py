from app.retrieval.evidence_retriever import EvidenceRetriever


def test_evidence_retriever():

    retriever = EvidenceRetriever()

    results = retriever.retrieve(
        "The laptop has a better GPU."
    )

    assert len(results) > 0

    print("\nEVIDENCE FOR CLAIM:\n")

    for document in results:
        print(document.page_content)
        print("-" * 60)