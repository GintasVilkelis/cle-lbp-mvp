from fastapi import FastAPI
from models import LBPRequest, LBPResponse
from engine import assess_low_back_pain

app = FastAPI(title="CLE LBP API")


@app.post("/api/lbp/assess", response_model=LBPResponse)
def assess_lbp(payload: LBPRequest):
    result = assess_low_back_pain(payload.dict())
    return result
