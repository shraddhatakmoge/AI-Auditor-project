from app.analyzers.decision_analyzer import DecisionAnalyzer


def test_decision_analyzer():

    analyzer = DecisionAnalyzer()

    result = analyzer.analyze(
        """
        I should buy the more expensive laptop because
        it has a better GPU and I want to use it for
        AI development.
        """
    )

    print("\nRESULT:")
    print(result)

    assert result.decision
    assert result.domain
    assert len(result.claims) > 0
    assert len(result.assumptions) > 0
    assert result.expected_outcome