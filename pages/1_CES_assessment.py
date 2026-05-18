import streamlit as st
from typing import Dict, Any
from engine import assess_low_back_pain

st.title("Cauda Equina Syndrome (CES) Screening")

from pathlib import Path

image_path = Path(__file__).parent.parent / "assets" / "diagrams" / "saddle_area_diagram.png"
if image_path.exists():
    st.image(str(image_path), caption="Saddle area (region where numbness is concerning)")
else:
    st.info("Saddle area diagram will appear here once added.")

# The below audio points to assets/audio/ces_explainer.mp3, which should be a concise explanation of CES red flags and urgency. This is separate from the general neuro symptoms explainer above, which can cover a broader range of symptoms and conditions.
# This is a different folder than what actually exists
audio_path = Path(__file__).parent.parent / "assets" / "audio" / "ces_explainer.mp3"
if audio_path.exists():
    st.audio(str(audio_path))
else:
    st.info("CES audio explanation will appear here once added.")

st.markdown(
    "This page focuses specifically on **cauda equina red flags**. "
    "If any of these are present, emergency assessment is required."
)

with st.form("ces_form"):
    st.subheader("Bladder and bowel function")
    urinary_retention = st.selectbox("Difficulty starting urination / urinary retention?", ["No", "Yes"])
    urinary_incontinence = st.selectbox("Loss of control of urination (incontinence)?", ["No", "Yes"])
    bowel_incontinence = st.selectbox("Loss of control of bowel movements?", ["No", "Yes"])

    st.subheader("Saddle area sensation")
    saddle_anaesthesia = st.selectbox(
        "Numbness or altered sensation in the area that would contact a saddle (inner thighs, perineum)?",
        ["No", "Yes"]
    )

    submitted = st.form_submit_button("Run CES assessment")

if submitted:
    # Minimal payload focused on CES; reuse existing structure
    payload: Dict[str, Any] = {
        "mode": "teaching",
        "patient": {
            "age": 45,
            "sex": "Other"
        },
        "pain": {
            "duration": "< 6 weeks",
            "onset": "Gradual",
            "location": "Central"
        },
        "red_flags": {
            "urinary_retention": urinary_retention,
            "urinary_incontinence": urinary_incontinence,
            "saddle_anaesthesia": saddle_anaesthesia,
            "bowel_incontinence": bowel_incontinence,
        }
    }

    result = assess_low_back_pain(payload)
    st.session_state["last_result"] = result

    st.subheader("Summary")
    st.write(result["summary"])

    if result["red_flags"]:
        st.error("Red flags detected:")
        for rf in result["red_flags"]:
            st.write(f"- {rf['label']}: {rf['reason']}")

    st.subheader("Possible conditions")
    for cond in result["conditions"]:
        st.markdown(f"**{cond['name']}** ({cond['likelihood']})")
        st.markdown(f"**Recommended routing:** {cond['routing']['description']}")
        st.markdown("---")

    # INSERT HERE
    if "reasoning_trace" in result and result["reasoning_trace"]:
        with st.expander("Show clinical reasoning trace"):
            for line in result["reasoning_trace"]:
                st.markdown(f"- {line}")

