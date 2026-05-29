from typing import Dict, Any
from backend.cle_lbp import run_lbp_engine

def assess_low_back_pain(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adapter between the frontend JSON schema and the NICE LBP engine.
    """

    # Adapt UI payload → engine input format
    engine_input: Dict[str, Any] = {
        "mode": payload.get("mode", "pro"),
        "patient": payload.get("patient", {}),
        "pain": payload.get("pain", {}),
        "red_flags": payload.get("red_flags", {})
    }

    # Run the full NICE engine
    engine_result: Dict[str, Any] = run_lbp_engine(engine_input)

    # Adapt engine output → API response format
    response: Dict[str, Any] = {
        "summary": engine_result.get("summary", ""),
        "red_flags": engine_result.get("red_flags", []),
        "conditions": engine_result.get("conditions", []),
        "question_explanations": engine_result.get("question_explanations", {}),
        "reasoning_trace": engine_result.get("reasoning_trace", [])
    }

    return response
