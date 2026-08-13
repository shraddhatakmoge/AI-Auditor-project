from app.prompts.decision_prompt import decision_prompt


def test_decision_prompt():

    result = decision_prompt.invoke({
        "decision": "I should buy the more expensive laptop because it has a better GPU and I want to use it for AI development."
    })

    assert result is not None
    assert len(result.messages) == 2