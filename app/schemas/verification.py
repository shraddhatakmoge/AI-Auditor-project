from enum import Enum

from pydantic import BaseModel, Field


class SupportStatus(str, Enum):
    SUPPORTED = "supported"
    PARTIALLY_SUPPORTED = "partially_supported"
    CONTRADICTED = "contradicted"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"


class EvidenceVerification(BaseModel):
    claim: str = Field(
        description="The claim being evaluated."
    )

    status: SupportStatus = Field(
        description="How strongly the evidence supports or contradicts the claim."
    )

    reasoning: str = Field(
        description="Brief explanation based only on the provided evidence."
    )

    confidence: float = Field(
        description="Confidence in the verification from 0.0 to 1.0."
    )