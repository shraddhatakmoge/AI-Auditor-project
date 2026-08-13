from app.analyzers.decision_analyzer import DecisionAnalyzer
from app.auditor.counterargument import CounterargumentEngine


def test_counterargument():

    analyzer = DecisionAnalyzer()

    decision_analysis = analyzer.analyze(
        """
        I should buy the more expensive laptop because
        it has a better GPU and I want to use it for AI development.
        """
    )

    engine = CounterargumentEngine()

    result = engine.generate(decision_analysis)

    print("\nCOUNTERARGUMENT\n")

    print("Argument:")
    print(result.argument)

    print("\nReasoning:")
    print(result.reasoning)

    print("\nImportance:")
    print(result.importance)

    assert result.argument
    assert result.reasoning
    assert result.importance