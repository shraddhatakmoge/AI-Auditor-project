from fastapi import FastAPI
from pydantic import BaseModel

from app.auditor.final_audit import FinalAuditor


app = FastAPI(
    title="AI Decision Auditor API",
    description="Backend API for the AI Decision Auditor",
    version="1.0.0"
)


auditor = FinalAuditor()


class AuditRequest(BaseModel):
    decision: str


@app.get("/")
def root():
    return {
        "message": "AI Decision Auditor API is running"
    }


@app.post("/audit")
def audit_decision(request: AuditRequest):

    result = auditor.audit(request.decision)

    return result