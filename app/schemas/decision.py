from pydantic import BaseModel, Field
from typing import List




class Assumption(BaseModel):
    text: str = Field(
        description="An assumption that must be true for the decision to make sense."
    )

    importance: str = Field(
        description="How important this assumption is to the decision: low, medium, or high."
    )


class DecisionAnalysis(BaseModel):
    decision: str = Field(
        description="The main decision the user is considering."
    )

    domain: str = Field(
        description="The general domain of the decision."
    )



    assumptions: List[Assumption] = Field(
        description="Important assumptions behind the decision."
    )

    expected_outcome: str = Field(
        description="The outcome the user expects from making this decision."
    )

    missing_information: List[str] = Field(
        description="Important information that is missing and could affect the decision."
    )