from typing import Dict, Any
from backend.cle_lbp import run_lbp_engine

def assess_low_back_pain(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adapter between the frontend JSON schema and the NICE LBP engine.
    """

    # 1) Convert boolean red_flags → "Yes"/"No" for the legacy engine
    raw_red_flags = payload.get("red_flags", {})
    engine_red_flags = {
        key: ("Yes" if value else "No")
        for key, value in raw_red_flags.items()
    }

    # 2) Build engine input
    engine_input: Dict[str, Any] = {
        "mode": payload.get("mode", "pro"),
        "patient": payload.get("patient", {}),
        "pain": payload.get("pain", {}),
        "red_flags": engine_red_flags,
    }

    # 3) Run the full NICE engine
    engine_result: Dict[str, Any] = run_lbp_engine(engine_input)

    # 4) Adapt engine output → API response format
    response: Dict[str, Any] = {
        "summary": engine_result.get("summary", ""),
        "red_flags": engine_result.get("red_flags", []),
        "conditions": engine_result.get("conditions", []),
        "question_explanations": engine_result.get("question_explanations") or {},
        "reasoning_trace": engine_result.get("reasoning_trace") or [],
    }

    return response
