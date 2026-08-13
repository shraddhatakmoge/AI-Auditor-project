from langchain_ollama import ChatOllama

from app.prompts.decision_prompt import decision_prompt
from app.schemas.decision import DecisionAnalysis


class DecisionAnalyzer:

    def __init__(self):
        self.llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
    think=False
)

        self.structured_llm = self.llm.with_structured_output(
            DecisionAnalysis
        )

        self.chain = decision_prompt | self.structured_llm

    def analyze(self, decision: str) -> DecisionAnalysis:
        return self.chain.invoke({
            "decision": decision
        })