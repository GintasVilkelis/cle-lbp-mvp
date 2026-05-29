from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import AssessmentRequest, AssessmentResponse
from backend.engine import assess_low_back_pain

app = FastAPI(
    title="CLE Low Back Pain API",
    description="FastAPI backend for the Clinical Logic Engine (CLE) MVP",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/lbp-assessment", response_model=AssessmentResponse)
def lbp_assessment(request: AssessmentRequest):
    """
    Accepts a JSON payload matching the Consumer/Pro schema,
    runs the NICE LBP engine, and returns a structured response.
    """
    payload = request.dict()
    result = assess_low_back_pain(payload)
    return AssessmentResponse(**result)
