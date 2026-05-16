from typing import Dict, Any

def assess_low_back_pain(payload: Dict[str, Any]) -> Dict[str, Any]:
    red_flags = []
    conditions = []

    # --- RED FLAGS ---
    if payload["red_flags"]["infection_signs"] == "Yes":
        red_flags.append({
            "code": "RF_INFECTION",
            "label": "Possible spinal infection",
            "reason": "Fever or systemic infection signs"
        })

    if payload["red_flags"]["bladder_bowel"] == "Yes":
        red_flags.append({
            "code": "RF_CES",
            "label": "Possible cauda equina syndrome",
            "reason": "Bladder/bowel dysfunction or saddle anaesthesia"
        })

    if payload["red_flags"]["cancer_history"] == "Yes":
        red_flags.append({
            "code": "RF_MALIGNANCY",
            "label": "Possible malignancy",
            "reason": "History of cancer"
        })

    # --- CONDITIONS ---
    if payload["pain"]["duration"] == "> 12 weeks":
        conditions.append({
            "code": "CHRONIC_LBP",
            "name": "Chronic low back pain",
            "likelihood": "high",
            "reasons": ["Pain duration > 12 weeks"],
            "routing": {
                "level": "primary_care",
                "description": "Consider physiotherapy and pain management."
            }
        })

    if not conditions:
        if red_flags:
            conditions.append({
                "code": "UNSPECIFIED_WITH_REDFLAGS",
                "name": "Low back pain with red flags",
                "likelihood": "undetermined",
                "reasons": [rf["label"] for rf in red_flags],
                "routing": {
                    "level": "urgent_care",
                    "description": "Urgent clinical assessment recommended due to red flags."
                }
            })
        else:
            conditions.append({
                "code": "NSLBP",
                "name": "Non-specific low back pain",
                "likelihood": "medium",
                "reasons": ["No red flags detected"],
                "routing": {
                    "level": "primary_care",
                    "description": "Conservative management recommended."
                }
            })

    # --- SUMMARY ---
    summary = (
        "Red flags detected — urgent assessment recommended."
        if red_flags else
        "No red flags detected. Likely non-specific low back pain."
    )

    # --- EXPLANATION MODE ---
    question_explanations = None
    if payload["mode"] == "teaching":
        question_explanations = {
            "recent_trauma": "Screens for fracture risk.",
            "cancer_history": "Screens for malignancy.",
            "infection_signs": "Screens for spinal infection.",
            "bladder_bowel": "Screens for cauda equina syndrome."
        }

    return {
        "summary": summary,
        "red_flags": red_flags,
        "conditions": conditions,
        "question_explanations": question_explanations
    }
