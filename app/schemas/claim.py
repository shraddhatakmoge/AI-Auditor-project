from enum import Enum

from pydantic import BaseModel, Field


class ClaimType(str, Enum):
    EXPLICIT = "explicit"
    INFERRED = "inferred"


class Verifiability(str, Enum):
    VERIFIABLE = "verifiable"
    SUBJECTIVE = "subjective"
    NOT_VERIFIABLE = "not_verifiable"


class Claim(BaseModel):
    text: str = Field(
        description="The factual or logical claim supporting the decision."
    )

    importance: str = Field(
        description="Importance of the claim: low, medium, or high."
    )

    claim_type: ClaimType = Field(
        description="Whether the claim was explicitly stated or inferred."
    )

    verifiability: Verifiability = Field(
        description="Whether the claim can be checked against external evidence."
    )