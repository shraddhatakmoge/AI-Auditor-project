from pydantic import BaseModel, Field


class Counterargument(BaseModel):
    argument: str = Field(
        description="The strongest reasonable argument against the user's decision."
    )

    reasoning: str = Field(
        description="Why this counterargument could materially weaken the decision."
    )

    importance: str = Field(
        description="Importance of this counterargument: low, medium, or high."
    )