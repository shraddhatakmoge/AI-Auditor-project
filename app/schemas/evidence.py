from pydantic import BaseModel, Field
from typing import List


class Evidence(BaseModel):
    claim: str = Field(
        description="The claim being investigated."
    )

    content: str = Field(
        description="Retrieved evidence relevant to the claim."
    )

    source: str = Field(
        description="Source of the retrieved evidence."
    )