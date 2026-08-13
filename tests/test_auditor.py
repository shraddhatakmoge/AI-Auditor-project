from app.auditor.auditor import Auditor
from app.schemas.claim import Claim, ClaimType, Verifiability


def test_auditor():

    claim = Claim(
        text="The RTX 4060 Laptop GPU generally provides higher compute performance than the RTX 4050 Laptop GPU.",
        importance="high",
        claim_type=ClaimType.EXPLICIT,
        verifiability=Verifiability.VERIFIABLE
    )

    auditor = Auditor()

    results = auditor.audit([claim])

    assert len(results) == 1

    result = results[0]

    print("\nAUDIT RESULT\n")

    print("Claim:")
    print(result.claim)

    print("\nImportance:")
    print(result.importance)

    print("\nStatus:")
    print(result.status.value)

    print("\nConfidence:")
    print(result.confidence)

    print("\nReasoning:")
    print(result.reasoning)

    print("\nEvidence:")

    for evidence in result.evidence:
        print("\nSource:", evidence.source)
        print(evidence.content)

    assert result.claim
    assert result.evidence
    assert result.reasoning
    assert 0.0 <= result.confidence <= 1.0