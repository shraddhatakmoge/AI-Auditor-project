from langchain_ollama import ChatOllama

from app.prompts.counterargument_prompt import counterargument_prompt
from app.schemas.counterargument import Counterargument


class CounterargumentEngine:

    def __init__(self):

        self.llm = ChatOllama(
            model="gemma3:1b",
            temperature=0,
            think=False
        )

        self.structured_llm = self.llm.with_structured_output(
            Counterargument
        )

        self.chain = counterargument_prompt | self.structured_llm

    def generate(self, decision_analysis):

        assumptions = "\n".join(
            f"- {assumption.text}"
            for assumption in decision_analysis.assumptions
        )

        missing_information = "\n".join(
            f"- {item}"
            for item in decision_analysis.missing_information
        )

        return self.chain.invoke(
            {
                "decision": decision_analysis.decision,
                "domain": decision_analysis.domain,
                "assumptions": assumptions,
                "expected_outcome": decision_analysis.expected_outcome,
                "missing_information": missing_information
            }
        )