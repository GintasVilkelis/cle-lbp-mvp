from fastapi import FastAPI
from models import LBPRequest, LBPResponse
from engine import assess_low_back_pain

app = FastAPI(title="CLE LBP API")

@app.post("/lbp-assessment", response_model=LBPResponse)
def assess_lbp(payload: LBPRequest):
    # Convert Pydantic model → dict
    request_dict = payload.dict()

    # Call your real clinical engine
    result = assess_low_back_pain(request_dict)

    return result
