from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="REPAIR-X API", version="0.1.0")

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/api/health", response_model=HealthResponse)
def health():
    return {"status": "ok", "service": "repair-x"}

@app.get("/api")
def api_root():
    return {
        "name": "REPAIR-X",
        "description": "AI Software Maintenance Engineer",
        "workflow": [
            "bug_report",
            "investigation",
            "reproduction",
            "root_cause",
            "fix_proposal",
            "approval",
            "patch",
            "tests",
            "impact_analysis",
            "proof_of_fix",
        ],
    }
