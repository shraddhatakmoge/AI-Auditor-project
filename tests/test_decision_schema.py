from app.schemas.decision import (
    DecisionAnalysis,
    Claim,
    Assumption
)


def test_decision_analysis():

    analysis = DecisionAnalysis(
        decision="Buy the more expensive laptop",
        domain="technology",

        claims=[
            Claim(
                text="The laptop has a better GPU",
                importance="high"
            ),
            Claim(
                text="The better GPU will improve AI development performance",
                importance="high"
            )
        ],

        assumptions=[
            Assumption(
                text="GPU performance is important for the user's workload",
                importance="high"
            ),
            Assumption(
                text="The performance improvement justifies the additional cost",
                importance="medium"
            )
        ],

        expected_outcome="Better AI development performance",

        missing_information=[
            "Actual AI workload",
            "GPU specifications",
            "Budget"
        ]
    )

    assert analysis.decision == "Buy the more expensive laptop"

    assert len(analysis.claims) == 2
    assert analysis.claims[0].text == "The laptop has a better GPU"
    assert analysis.claims[0].importance == "high"

    assert len(analysis.assumptions) == 2
    assert analysis.assumptions[0].importance == "high"