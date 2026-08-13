from langchain_ollama import ChatOllama

from app.prompts.claim_prompt import claim_prompt
from app.schemas.claim import ClaimAnalysis


class ClaimAnalyzer:

    def __init__(self):
        self.llm = ChatOllama(
            model="qwen3:8b",
            temperature=0,
            think=False
        )

        self.structured_llm = self.llm.with_structured_output(
            ClaimAnalysis
        )

        self.chain = claim_prompt | self.structured_llm

    def analyze(self, claim: str) -> ClaimAnalysis:
        return self.chain.invoke({
            "claim": claim
        })