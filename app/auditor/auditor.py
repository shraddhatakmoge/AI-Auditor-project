from app.retrieval.evidence_retriever import EvidenceRetriever
from app.auditor.evidence_verifier import EvidenceVerifier
from app.schemas.audit import AuditResult, EvidenceItem


class Auditor:

    def __init__(self):
        self.retriever = EvidenceRetriever()
        self.verifier = EvidenceVerifier()

    def audit_claim(self, claim):

        if claim.verifiability.value != "verifiable":
            return None

        documents = self.retriever.retrieve(claim.text)

        if not documents:
            return None

        evidence_text = "\n\n".join(
            document.page_content
            for document in documents
        )

        verification = self.verifier.verify(
            claim=claim.text,
            evidence=evidence_text
        )

        evidence_items = [
            EvidenceItem(
                content=document.page_content,
                source=document.metadata.get(
                    "source",
                    "unknown"
                )
            )
            for document in documents
        ]

        return AuditResult(
            claim=claim.text,
            importance=claim.importance.value
            if hasattr(claim.importance, "value")
            else claim.importance,
            status=verification.status,
            evidence=evidence_items,
            reasoning=verification.reasoning,
            confidence=verification.confidence
        )

    def audit(self, claims):

        results = []

        for claim in claims:

            result = self.audit_claim(claim)

            if result is not None:
                results.append(result)

        return results