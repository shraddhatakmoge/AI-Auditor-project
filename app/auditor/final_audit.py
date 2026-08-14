from app.analyzers.decision_analyzer import DecisionAnalyzer
from app.auditor.counterargument import CounterargumentEngine
from app.auditor.evidence_verifier import EvidenceVerifier
from app.auditor.risk import calculate_overall_risk
from app.retrieval.retriever import create_retriever


class FinalAuditor:

    def __init__(self):

        self.decision_analyzer = DecisionAnalyzer()
        self.retriever = create_retriever()
        self.evidence_verifier = EvidenceVerifier()
        self.counterargument_engine = CounterargumentEngine()

    def audit(self, decision: str):

        # 1. Analyze decision
        analysis = self.decision_analyzer.analyze(decision)

        # 2. Retrieve relevant evidence
        documents = self.retriever.invoke(decision)

        # 3. Verify only when relevant evidence exists
        if documents:

            evidence = "\n\n".join(
                document.page_content
                for document in documents
            )

            verification = self.evidence_verifier.verify(
                claim=decision,
                evidence=evidence
            )

        else:

            # No relevant evidence was found
            verification = self.evidence_verifier.no_evidence()

        # 4. Calculate risk
        risk = calculate_overall_risk(
            [verification],
            analysis.assumptions,
            analysis.missing_information
        )

        # 5. Generate counterargument
        counterargument = self.counterargument_engine.generate(
            analysis
        )

        return {
            "decision": analysis.decision,
            "domain": analysis.domain,
            "assumptions": analysis.assumptions,
            "expected_outcome": analysis.expected_outcome,
            "missing_information": analysis.missing_information,
            "verification": verification,
            "evidence": documents,
            "risk": risk,
            "counterargument": counterargument
        }