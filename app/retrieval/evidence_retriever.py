from app.retrieval.retriever import create_retriever


class EvidenceRetriever:

    def __init__(self):
        self.retriever = create_retriever()

    def retrieve(self, claim: str):

        documents = self.retriever.invoke(claim)

        return documents