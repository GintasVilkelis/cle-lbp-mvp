from pydantic import BaseModel
from typing import List, Optional, Literal, Dict


# -----------------------------
# INPUT MODELS
# -----------------------------

class PatientInfo(BaseModel):
    age: int
    sex: Literal["Male", "Female", "Other"]


class PainInfo(BaseModel):
    duration: Literal["< 6 weeks", "6–12 weeks", "> 12 weeks"]
    onset: Literal["Sudden", "Gradual"]
    location: Literal["Central", "Unilateral", "Bilateral", "Radiating to leg"]


class RedFlagInfo(BaseModel):
    recent_trauma: Literal["Yes", "No"]
    cancer_history: Literal["Yes", "No"]
    weight_loss: Literal["Yes", "No"]
    infection_signs: Literal["Yes", "No"]
    steroid_use: Literal["Yes", "No"]
    iv_drug_use: Literal["Yes", "No"]
    immunosuppression: Literal["Yes", "No"]
    night_pain: Literal["Yes", "No"]
    neuro_deficit: Literal["Yes", "No"]
    bladder_bowel: Literal["Yes", "No"]


class LBPRequest(BaseModel):
    mode: Literal["teaching", "pro"]
    patient: PatientInfo
    pain: PainInfo
    red_flags: RedFlagInfo


# -----------------------------
# OUTPUT MODELS
# -----------------------------

class RoutingInfo(BaseModel):
    level: Literal["self_care", "primary_care", "urgent_care", "emergency"]
    description: str


class ConditionInfo(BaseModel):
    code: str
    name: str
    likelihood: Literal["low", "medium", "high"]
    reasons: Optional[List[str]] = None
    routing: RoutingInfo


class RedFlagDetected(BaseModel):
    code: str
    label: str
    reason: str


class LBPResponse(BaseModel):
    summary: str
    red_flags: List[RedFlagDetected]
    conditions: List[ConditionInfo]
    question_explanations: Optional[Dict[str, str]] = None
