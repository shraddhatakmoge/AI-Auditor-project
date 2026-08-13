from app.analyzers.claim_analyzer import ClaimAnalyzer


def test_claim_analyzer():

    analyzer = ClaimAnalyzer()

    result = analyzer.analyze(
        "The more expensive laptop has a better GPU."
    )

    print("\nCLAIM ANALYSIS:")
    print(result)

    assert result.text
    assert result.claim_type
    assert result.verifiability
    assert result.reason