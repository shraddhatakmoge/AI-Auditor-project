from app.analyzers.decision_analyzer import DecisionAnalyzer
from app.analyzers.claim_analyzer import ClaimAnalyzer


class DecisionPipeline:

    def __init__(self):
        self.decision_analyzer = DecisionAnalyzer()
        self.claim_analyzer = ClaimAnalyzer()

    def analyze(self, decision: str):

        # Step 1: Analyze the overall decision
        decision_analysis = self.decision_analyzer.analyze(decision)

        # Step 2: Analyze every extracted claim
        claim_analyses = []

        for claim in decision_analysis.claims:
            analysis = self.claim_analyzer.analyze(claim.text)
            claim_analyses.append(analysis)

        return {
            "decision_analysis": decision_analysis,
            "claim_analyses": claim_analyses
        }