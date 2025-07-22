import streamlit as st
from pages import login, signup, feedback, report

st.set_page_config(page_title="AI Health Assistant", layout="centered")

# Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "username" not in st.session_state:
    st.session_state.username = ""

# --- NOT LOGGED IN ---
if not st.session_state.logged_in:
    st.sidebar.title("Authentication")
    st.session_state.page = st.sidebar.radio("Choose", ["Login", "Signup"])

    if st.session_state.page == "Login":
        login.show_login_page()
    else:
        signup.show_signup_page()

# --- LOGGED IN ---
else:
    st.title(f"🩺 Welcome, {st.session_state.username}")
    st.sidebar.title("📌 Navigation")

    page = st.sidebar.radio("Go to", [
        "Chat with Assistant",
        "Generate Report",
        "Nearby Hospitals",
        "Feedback",
        "Logout"
    ])

    if page == "Chat with Assistant":
        from pages import chatbot
        chatbot.show_chatbot_page()

    elif page == "Generate Report":
        report.show_report_page()

    elif page == "Nearby Hospitals":
        from pages import hospital
        hospital.show_hospital_page()

    elif page == "Feedback":
        feedback.show_feedback_page()

    elif page == "Logout":
        for key in list(st.session_state.keys()):
            del st.session_state[key]  
        st.rerun() 
