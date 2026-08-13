from pydantic import BaseModel, Field

from app.schemas.verification import SupportStatus


class EvidenceItem(BaseModel):
    content: str = Field(
        description="The retrieved evidence supporting or contradicting the claim."
    )

    source: str = Field(
        description="The source from which the evidence was retrieved."
    )


class AuditResult(BaseModel):
    claim: str = Field(
        description="The claim being audited."
    )

    importance: str = Field(
        description="Importance of the claim: low, medium, or high."
    )

    status: SupportStatus = Field(
        description="Whether the evidence supports, partially supports, contradicts, or is insufficient for the claim."
    )

    evidence: list[EvidenceItem] = Field(
        description="Evidence retrieved for the claim."
    )

    reasoning: str = Field(
        description="Explanation of why the evidence leads to the verification result."
    )

    confidence: float = Field(
        description="Confidence in the verification from 0.0 to 1.0."
    )