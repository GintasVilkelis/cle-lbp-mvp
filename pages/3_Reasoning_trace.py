import streamlit as st
from engine import assess_low_back_pain

st.title("Clinical Reasoning Trace")

st.markdown(
    "This page displays the full reasoning trace from the NICE LBP engine. "
    "Run an assessment on any page, then return here to view the trace."
)

if "last_result" not in st.session_state:
    st.info("Run an assessment first.")
else:
    result = st.session_state["last_result"]
    if "reasoning_trace" in result:
        for line in result["reasoning_trace"]:
            st.markdown(f"- {line}")
    else:
        st.info("No reasoning trace available.")
