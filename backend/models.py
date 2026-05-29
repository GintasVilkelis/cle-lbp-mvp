from typing import Optional, Dict, Any, List
from pydantic import BaseModel


# ---------------------------------------------------------
# INPUT MODELS (what the frontend sends)
# ---------------------------------------------------------

class PatientInfo(BaseModel):
    age: Optional[int] = None
    sex: Optional[str] = None   # "male" | "female" | "other"


class PainInfo(BaseModel):
    duration: Optional[str] = None
    onset: Optional[str] = None
    location: Optional[str] = None


class AssessmentRequest(BaseModel):
    """
    This matches EXACTLY what the React frontend sends.
    It also matches what backend.engine.assess_low_back_pain expects.
    """
    mode: str                       # "consumer" | "pro" | "teaching"
    patient: Dict[str, Any]         # { age, sex }
    pain: Dict[str, Any]            # { duration, onset, location }
    red_flags: Dict[str, Any]       # all red flag answers


# ---------------------------------------------------------
# OUTPUT MODELS (what the backend returns)
# ---------------------------------------------------------

class RedFlag(BaseModel):
    code: str
    label: str
    reason: Optional[str] = None


class Condition(BaseModel):
    code: str
    name: str
    likelihood: Optional[str] = None
    reasons: Optional[List[str]] = None
    routing: Optional[Dict[str, Any]] = None
    severity: Optional[int] = None
    score: Optional[float] = None


class AssessmentResponse(BaseModel):
    """
    This matches EXACTLY what backend.engine.assess_low_back_pain returns.
    It also matches what the React Results page expects.
    """
    summary: str
    red_flags: List[RedFlag]
    conditions: List[Condition]
    question_explanations: Dict[str, Any] = {}
    reasoning_trace: List[Any] = []
