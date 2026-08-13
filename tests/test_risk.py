from app.auditor.risk import calculate_overall_risk
from app.schemas.audit import AuditResult
from app.schemas.verification import SupportStatus


def test_risk_calculation():

    results = [
        AuditResult(
            claim="The laptop has a better GPU.",
            importance="high",
            status=SupportStatus.SUPPORTED,
            evidence=[],
            reasoning="Evidence supports the claim.",
            confidence=0.95
        ),

        AuditResult(
            claim="The GPU is necessary for my workload.",
            importance="high",
            status=SupportStatus.INSUFFICIENT_EVIDENCE,
            evidence=[],
            reasoning="The workload is not specified.",
            confidence=0.90
        )
    ]

    risk = calculate_overall_risk(results)

    print("\nRISK:")
    print(risk)

    assert risk["score"] == 9
    assert risk["level"] == "high"