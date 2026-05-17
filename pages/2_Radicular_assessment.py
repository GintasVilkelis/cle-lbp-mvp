import streamlit as st
from engine import assess_low_back_pain

st.title("Radicular Pain / Sciatica Assessment")

from pathlib import Path

image_path = Path(__file__).parent.parent / "assets" / "dermatomes.webp"
if image_path.exists():
    st.image(str(image_path), caption="Dermatomal map")
else:
    st.info("Dermatomal map will appear here once added.")

st.markdown(
    "This page focuses on symptoms related to **nerve root compression**, "
    "including dermatomal pain patterns and neurological deficits."
)

with st.form("radicular_form"):

    st.subheader("Leg pain distribution (dermatomes)")
    dermatome_region = st.selectbox(
        "Where is the leg pain or altered sensation most prominent?",
        [
            "None / not applicable",
            "Front of thigh (L2–L3)",
            "Inner knee / medial leg (L3–L4)",
            "Top of foot / big toe (L4–L5)",
            "Outer leg / little toe (L5–S1)",
            "Back of thigh / calf (S1)",
            "Perineal / saddle area (S2–S4)"
        ]
    )

    st.subheader("Neurological symptoms")
    leg_pain_worse_than_back = st.selectbox("Leg pain worse than back pain?", ["No", "Yes"])
    positive_slr = st.selectbox("Positive straight-leg raise test?", ["No", "Yes"])
    sensory_changes = st.selectbox("Sensory changes (numbness/tingling)?", ["No", "Yes"])
    motor_weakness = st.selectbox("Motor weakness in the leg?", ["No", "Yes"])
    reflex_changes = st.selectbox("Reflex changes?", ["No", "Yes"])

    submitted = st.form_submit_button("Run radicular assessment")

if submitted:
    payload = {
        "mode": "teaching",
        "patient": {"age": 45, "sex": "Other"},
        "pain": {"duration": "< 6 weeks", "onset": "Gradual", "location": "Central"},
        "red_flags": {
            "dermatomal_distribution": dermatome_region != "None / not applicable",
            "leg_pain_worse_than_back": leg_pain_worse_than_back,
            "positive_slr": positive_slr,
            "sensory_changes": sensory_changes,
            "motor_weakness_radicular": motor_weakness,
            "reflex_changes": reflex_changes,
        }
    }

    result = assess_low_back_pain(payload)

    st.subheader("Summary")
    st.write(result["summary"])

    st.subheader("Possible conditions")
    for cond in result["conditions"]:
        st.markdown(f"**{cond['name']}** ({cond['likelihood']})")
        st.markdown(f"**Routing:** {cond['routing']['description']}")
        st.markdown("---")

        if "reasoning_trace" in result and result["reasoning_trace"]:
            with st.expander("Show clinical reasoning trace"):
                for line in result["reasoning_trace"]:
                    st.markdown(f"- {line}")
