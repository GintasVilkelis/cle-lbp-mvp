# app.py
import streamlit as st
from typing import Dict, Any
import importlib
import engine
importlib.reload(engine)
from engine import assess_low_back_pain  # your engine module

st.set_page_config(page_title="Low Back Pain Assessment", layout="centered")

st.title("Low Back Pain Assessment (MVP)")
st.markdown("Structured assessment based on guideline-style logic. Not a substitute for clinical judgement.")

mode = st.radio("Mode", ["Teaching mode", "Pro mode"])

with st.form("lbp_form"):
    st.subheader("Patient details")
    age = st.number_input("Age", min_value=0, max_value=120, value=45)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])

    st.subheader("Pain characteristics")
    duration = st.selectbox(
        "How long has the back pain been present?",
        ["< 6 weeks", "6–12 weeks", "> 12 weeks"]
    )
    onset = st.selectbox(
        "Onset of pain",
        ["Sudden", "Gradual"]
    )
    location = st.selectbox(
        "Pain location",
        [
            "Central",
            "Left-sided",
            "Right-sided",
            "Bilateral (left worse)",
            "Bilateral (right worse)",
            "Radiating to left leg",
            "Radiating to right leg",
            "Radiating to both legs"
        ]
    )

    st.subheader("Red flag screening")
    recent_trauma = st.selectbox("Recent significant trauma?", ["No", "Yes"])
    minor_trauma_elderly = st.selectbox("Minor trauma in older adult?", ["No", "Yes"])
    cancer_history = st.selectbox("History of cancer?", ["No", "Yes"])
    weight_loss = st.selectbox("Unexplained weight loss?", ["No", "Yes"])
    night_pain = st.selectbox("Night pain or pain at rest?", ["No", "Yes"])
    infection_signs = st.selectbox("Fever or recent infection?", ["No", "Yes"])
    iv_drug_use = st.selectbox("IV drug use?", ["No", "Yes"])
    immunosuppression = st.selectbox("Immunosuppression?", ["No", "Yes"])
    steroid_use = st.selectbox("Prolonged corticosteroid use?", ["No", "Yes"])
    neuro_deficit = st.selectbox("Progressive neurological deficit?", ["No", "Yes"])
    bladder_bowel = st.selectbox("Bladder/bowel dysfunction or saddle anaesthesia?", ["No", "Yes"])

    if mode == "Teaching mode":
        st.markdown("### Why these questions matter")
        st.markdown("- **Recent trauma:** screens for fracture risk.")
        st.markdown("- **Cancer history / weight loss / night pain:** screens for malignancy.")
        st.markdown("- **Fever / IV drug use / immunosuppression:** screens for spinal infection.")
        st.markdown("- **Bladder/bowel / saddle anaesthesia:** screens for cauda equina syndrome.")
        st.markdown("- **Progressive neurological deficit:** indicates possible serious nerve compromise.")

    submitted = st.form_submit_button("Run assessment")

if submitted:
    payload: Dict[str, Any] = {
        "mode": "teaching" if mode == "Teaching mode" else "pro",
        "patient": {
            "age": age,
            "sex": sex
        },
        "pain": {
            "duration": duration,
            "onset": onset,
            "location": location
        },
        "red_flags": {
            "recent_trauma": recent_trauma,
            "cancer_history": cancer_history,
            "weight_loss": weight_loss,
            "infection_signs": infection_signs,
            "steroid_use": steroid_use,
            "iv_drug_use": iv_drug_use,
            "immunosuppression": immunosuppression,
            "night_pain": night_pain,
            "neuro_deficit": neuro_deficit,
            "bladder_bowel": bladder_bowel
        }
    }

    result = assess_low_back_pain(payload)

    st.subheader("Summary")
    st.write(result["summary"])

    if result["red_flags"]:
        st.error("Red flags detected:")
        for rf in result["red_flags"]:
            st.write(f"- {rf}")

    st.subheader("Possible conditions")
    for cond in result["conditions"]:
        st.markdown(f"**{cond['name']}** ({cond['likelihood']})")
        st.markdown(f"**Recommended routing:** {cond['routing']['description']}")
        if mode == "Teaching mode":
            st.markdown("**Reasons:**")
            for r in cond["reasons"]:
                st.markdown(f"- {r}")
        st.markdown("---")
        
        # INSERT HERE
        if "reasoning_trace" in result and result["reasoning_trace"]:
            with st.expander("Show clinical reasoning trace"):
                for line in result["reasoning_trace"]:
                    st.markdown(f"- {line}")
        
        import json
        report = json.dumps(result, indent=2)
        st.download_button(
            label="Download full report",
            data=report,
            file_name="lbp_assessment.json",
            mime="application/json"
        )

