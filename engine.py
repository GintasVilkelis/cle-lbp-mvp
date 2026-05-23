from typing import Dict, Any
from cle_lbp import run_lbp_engine  # import your full NICE engine


def assess_low_back_pain(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Wrapper between Streamlit/FastAPI and the full NICE LBP engine.

    1. Accepts validated input from the UI (payload)
    2. Adapts it to the engine's expected input format
    3. Calls run_lbp_engine(...)
    4. Adapts the engine's output to the API response format used by app.py
    """

    # 1) Adapt UI payload → engine input format
    engine_input: Dict[str, Any] = {
        "mode": payload["mode"],          # "teaching" or "pro"
        "patient": payload["patient"],    # age, sex
        "pain": payload["pain"],          # duration, onset, location
        "red_flags": payload["red_flags"] # all red flag answers
    }

    # 2) Call the full NICE engine
    engine_result: Dict[str, Any] = run_lbp_engine(engine_input)

    # We now assume engine_result looks something like:
    # {
    #   "summary": str,
    #   "red_flags": [ { "code": ..., "label": ..., "reason": ... }, ... ],
    #   "conditions": [
    #       {
    #           "code": ...,
    #           "name": ...,
    #           "likelihood": "low|medium|high",
    #           "reasons": [...],
    #           "routing": {
    #               "level": "self_care|primary_care|urgent_care|emergency",
    #               "description": str
    #           },
    #           "severity": int,          # optional
    #           "score": float            # optional
    #       },
    #       ...
    #   ],
    #   "reasoning_trace": [...],         # optional
    #   "question_explanations": {...}    # optional
    # }

    # 3) Adapt engine_result → API response format expected by app.py
    # Right now, app.py expects:
    # {
    #   "summary": str,
    #   "red_flags": [...],
    #   "conditions": [...],
    #   "question_explanations": Optional[dict]
    # }

    response: Dict[str, Any] = {
    "summary": engine_result.get("summary", ""),
    "red_flags": engine_result.get("red_flags", []),
    "conditions": engine_result.get("conditions", []),
    "question_explanations": engine_result.get("question_explanations", {})
    }

    # Later, we can extend app.py to also show:
    # - engine_result["reasoning_trace"]
    # - severity, scores, etc.

    # Ensure required fields exist
    response.setdefault("reasoning_trace", [])

    return response