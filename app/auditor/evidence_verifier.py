from langchain_ollama import ChatOllama

from app.prompts.verification_prompt import verification_prompt
from app.schemas.verification import (
    EvidenceVerification,
    SupportStatus
)


class EvidenceVerifier:

    def __init__(self):

        self.llm = ChatOllama(
            model="gemma3:1b",
            temperature=0,
            think=False
        )

        self.structured_llm = self.llm.with_structured_output(
            EvidenceVerification
        )

        self.chain = verification_prompt | self.structured_llm

    def verify(
        self,
        claim: str,
        evidence: str
    ) -> EvidenceVerification:

        return self.chain.invoke(
            {
                "claim": claim,
                "evidence": evidence
            }
        )

    def no_evidence(self) -> EvidenceVerification:

        return EvidenceVerification(
            claim="No relevant evidence found",
            status=SupportStatus.INSUFFICIENT_EVIDENCE,
            reasoning=(
                "No relevant evidence was found in the current "
                "knowledge base, so the decision cannot be verified "
                "against external evidence."
            ),
            confidence=0.0
        )