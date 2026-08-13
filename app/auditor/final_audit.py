from app.auditor.auditor import Auditor
from app.auditor.counterargument import CounterargumentEngine
from app.auditor.risk import calculate_overall_risk
from app.analyzers.decision_analyzer import DecisionAnalyzer


class FinalAuditor:

    def __init__(self):
        self.decision_analyzer = DecisionAnalyzer()
        self.auditor = Auditor()
        self.counterargument_engine = CounterargumentEngine()

    def audit(self, decision: str):

        # 1. Analyze the user's decision
        analysis = self.decision_analyzer.analyze(decision)

        # 2. Verify claims using RAG evidence
        audit_results = self.auditor.audit(
            analysis.claims
        )

        # 3. Calculate deterministic risk
        risk = calculate_overall_risk(
    audit_results,
    analysis.assumptions,
    analysis.missing_information
)

        # 4. Generate strongest counterargument
        counterargument = self.counterargument_engine.generate(
            analysis
        )

        return {
            "decision": analysis.decision,
            "domain": analysis.domain,
            "claims": analysis.claims,
            "assumptions": analysis.assumptions,
            "expected_outcome": analysis.expected_outcome,
            "missing_information": analysis.missing_information,
            "audit_results": audit_results,
            "risk": risk,
            "counterargument": counterargument
        }