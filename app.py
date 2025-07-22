import streamlit as st
from pages import login,signup
from pages import feedback
from pages import report


st.set_page_config(page_title="AI Health Assistant",layout= "centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Login"

# Choose page
if not st.session_state.logged_in:
    st.sidebar.title("Authentication")
    st.session_state.page = st.sidebar.radio("Choose", ["Login", "Signup"])

    if st.session_state.page == "Login":
        login.show_login_page()
    else:
        signup.show_signup()

else:
    st.title("🩺 AI Health Assistant")
    st.sidebar.title("📌 Navigation")
    page = st.sidebar.radio("Go to",["chat with Assistant", "Generate Report","Nearby Hospitals", "Feedback", "Logout"])
    
    if page == "chat with Assistant":
        from pages import chatbot
        chatbot.show_chatbot_page()

    elif page == "Generate Report":
        from pages import report
        report.show_report_page()
    
    elif page == "Nearby Hospitals":
        from pages import hospital
        hospital.show_hospital_page()

    elif page == "Feedback":
        from pages import feedback
        feedback.show_feedback_page()

    elif page == "Logout":
        st.session_state.logged_in = False
        st.rerun()