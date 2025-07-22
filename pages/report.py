import os
import streamlit as st
from utils.pdf_generator import create_pdf

def show_report_page():
    st.subheader("📝 Generate Health Report")

    name = st.text_input("Enter your name")
    symptoms_input = st.text_area("Enter symptoms (comma separated)")

    if st.button("Generate Report"):
        if name and symptoms_input:
            symptoms_list = [sym.strip() for sym in symptoms_input.split(",")]
            file_path = create_pdf(name, symptoms_list)

            with open(file_path, "rb") as f:
                st.success("✅ Report Generated!")
                st.download_button(
                    label="📥 Download Report",
                    data=f,
                    file_name=file_path,
                    mime="application/pdf"
                )
        else:
            st.error("Please enter both name and symptoms.")
