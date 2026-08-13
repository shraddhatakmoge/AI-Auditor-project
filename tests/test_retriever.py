from app.retrieval.retriever import create_retriever


def test_retriever():

    retriever = create_retriever()

    results = retriever.invoke(
        "Does a better GPU help with AI development?"
    )

    assert len(results) > 0

    print("\nRETRIEVED EVIDENCE:\n")

    for document in results:
        print(document.page_content)
        print("-" * 60)