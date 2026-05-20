from pydantic import BaseModel
from typing import Dict, Any, List, Optional


# -----------------------------
# Request Models
# -----------------------------

class PatientModel(BaseModel):
    age: int
    sex: str


class PainModel(BaseModel):
    duration: str
    onset: str
    location: str


class RedFlagsModel(BaseModel):
    # CES fields (may come from CES page or main app page)
    urinary_retention: Optional[str] = None
    urinary_incontinence: Optional[str] = None
    saddle_anaesthesia: Optional[str] = None
    bowel_incontinence: Optional[str] = None

    # Combined field from main app page
    bladder_bowel: Optional[str] = None

    # Radicular fields
    leg_pain_worse_than_back: Optional[str] = None
    dermatomal_distribution: Optional[str] = None
    positive_slr: Optional[str] = None
    sensory_changes: Optional[str] = None
    motor_weakness_radicular: Optional[str] = None
    reflex_changes: Optional[str] = None


class AssessmentRequest(BaseModel):
    mode: str
    patient: PatientModel
    pain: PainModel
    red_flags: RedFlagsModel


# -----------------------------
# Response Models
# -----------------------------

class RedFlagOutput(BaseModel):
    code: str
    label: str
    reason: str


class ConditionOutput(BaseModel):
    code: str
    name: str
    likelihood: str
    reasons: List[str]
    routing: Dict[str, Any]


class AssessmentResponse(BaseModel):
    summary: str
    red_flags: List[RedFlagOutput]
    conditions: List[ConditionOutput]
    reasoning_trace: List[str]
    question_explanations: Dict[str, Any]
