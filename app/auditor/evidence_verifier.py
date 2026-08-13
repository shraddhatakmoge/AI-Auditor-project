from langchain_ollama import ChatOllama

from app.prompts.verification_prompt import verification_prompt
from app.schemas.verification import EvidenceVerification


class EvidenceVerifier:

    def __init__(self):

        self.llm = ChatOllama(
            model="qwen3:8b",
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