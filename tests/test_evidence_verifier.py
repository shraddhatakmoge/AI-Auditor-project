from app.auditor.evidence_verifier import EvidenceVerifier


def test_evidence_verifier():

    verifier = EvidenceVerifier()

    claim = "The RTX 4060 Laptop GPU has higher compute performance than the RTX 4050 Laptop GPU."

    evidence = """
    Laptop A has an NVIDIA RTX 4060 Laptop GPU with 8 GB of VRAM.
    Laptop B has an NVIDIA RTX 4050 Laptop GPU with 6 GB of VRAM.

    The RTX 4060 Laptop GPU generally provides higher graphics and compute
    performance than the RTX 4050 Laptop GPU.
    """

    result = verifier.verify(
        claim=claim,
        evidence=evidence
    )

    print("\nVERIFICATION RESULT:\n")
    print("Claim:", result.claim)
    print("Status:", result.status.value)
    print("Reasoning:", result.reasoning)
    print("Confidence:", result.confidence)

    assert result.claim
    assert result.status
    assert result.reasoning
    assert 0.0 <= result.confidence <= 1.0