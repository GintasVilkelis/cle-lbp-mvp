from typing import Dict, Any

def assess_low_back_pain(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calls your internal LBP engine (or FastAPI later).
    Expects a structured payload, returns structured result.
    """
    # TODO: replace with real engine call
    return {
        "summary": "No red flags detected. Likely non-specific low back pain.",
        "red_flags": [],
        "conditions": [
            {
                "code": "NSLBP",
                "name": "Non-specific low back pain",
                "likelihood": "high",
                "reasons": [
                    "Pain duration between 6–12 weeks",
                    "No red flags present"
                ],
                "routing": {
                    "level": "primary_care",
                    "description": "Manage in primary care with conservative treatment."
                }
            }
        ],
        "question_explanations": {
            "recent_trauma": "Significant trauma raises suspicion for vertebral fracture.",
            "cancer_history": "History of cancer raises suspicion for metastatic disease.",
            "bladder_bowel": "Bladder/bowel dysfunction may indicate cauda equina syndrome."
        }
    }
