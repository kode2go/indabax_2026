# indabax_page.py
import streamlit as st

st.set_page_config(
    page_title="AI Guidelines for Infrastructure as a Service Platforms",
    page_icon="☁️",
    layout="centered"
)

st.title("IndabaX 2026")
st.subheader("AI Guidelines for Infrastructure as a Service Platforms")

st.markdown(
    """
Thank you for attending the talk.

This page brings together the key links mentioned during the session.
"""
)

st.divider()

st.header("Talk Slides")
st.markdown(
    """
Download or view the slides from the IndabaX talk:
"""
)

st.link_button(
    "📄 Download Talk Slides (PDF)",
    "https://raw.githubusercontent.com/kode2go/indabax_2026/main/Developing_AI_Guidelines_for_Infrastructure_as_a_Service_Platforms_v4.pdf"
)

st.divider()

st.header("Try VuthaStack")
st.markdown(
    """
**VuthaStack — VMs in Minutes**

Interested in trying local virtual machines hosted in South Africa?

Fill in the expression of interest form below.
"""
)
st.link_button(
    "Fill in VuthaStack Form",
    "https://forms.cloud.microsoft/r/QbHnRehVYy"
)

st.divider()

st.header("CHPC Access")
st.markdown(
    """
To know more about CHPC and gain access to local compute and cloud resources:
"""
)
st.link_button("Visit CHPC", "https://chpc.ac.za")

st.caption("CHPC | Local compute, cloud access, and responsible AI infrastructure")
