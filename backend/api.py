from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import AssessmentRequest, AssessmentResponse
from backend.engine import assess_low_back_pain

app = FastAPI(
    title="CLE Low Back Pain API",
    description="FastAPI backend for the Clinical Logic Engine (CLE) MVP",
    version="1.0.0"
)

# ---------------------------------------------------------
# CORS (allow React frontend + Streamlit to call the API)
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For MVP; later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Health check endpoint
# ---------------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# ---------------------------------------------------------
# Main LBP assessment endpoint
# ---------------------------------------------------------
@app.post("/lbp-assessment", response_model=AssessmentResponse)
def lbp_assessment(request: AssessmentRequest):
    """
    Accepts a JSON payload matching the Streamlit schema,
    runs the NICE LBP engine, and returns a structured response.
    """

    # Convert Pydantic model → dict for your engine
    payload = request.dict()

    # Run your existing engine
    result = assess_low_back_pain(payload)

    # Return the result exactly as your engine produces it
    return AssessmentResponse(**result)
