# feedback.py
import streamlit as st

def show_feedback_page():
    st.subheader("📣 Feedback")
    st.write("We value your feedback. Please let us know what you think!")
    feedback = st.text_area("How was your experience ?")

    if st.button("submit Feedback"):
        if feedback:
            st.success("Thankyou for your Feedback!")
        else:
            st.warning("Please write something before submitting")

