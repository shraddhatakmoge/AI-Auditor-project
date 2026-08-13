from pydantic import BaseModel, Field

from app.schemas.audit import AuditResult
from app.schemas.claim import Assumption
from app.schemas.decision import DecisionAnalysis


class DecisionAuditReport(BaseModel):
    decision: str = Field(
        description="The decision being audited."
    )

    domain: str = Field(
        description="The domain of the decision."
    )

    claims: list = Field(
        description="Claims identified from the decision."
    )

    assumptions: list[Assumption] = Field(
        description="Assumptions identified from the decision."
    )

    expected_outcome: str = Field(
        description="The expected outcome of the decision."
    )

    missing_information: list[str] = Field(
        description="Important information missing from the decision."
    )

    evidence_audits: list[AuditResult] = Field(
        description="Evidence-based audit results for verifiable claims."
    )