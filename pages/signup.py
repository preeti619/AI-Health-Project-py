# pages/signup.py
import streamlit as st
from utils.db_helper import add_user

def show_signup_page():
    st.title("📝 Sign Up")

    username = st.text_input("👤 Username")
    full_name = st.text_input("🧾 Full Name")
    phone = st.text_input("📱 Phone Number")
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    confirm_password = st.text_input("🔒 Confirm Password", type="password")
    address = st.text_area("🏠 Address")

    if st.button("Create Account"):
        if not all([username, full_name, phone, email, password, confirm_password, address]):
            st.warning("⚠️ Please fill all fields.")
        elif password != confirm_password:
            st.warning("❌ Passwords do not match.")
        else:
            try:
                add_user(username, full_name, phone, email, password, address)
                st.success("🎉 Account created successfully. Please login.")
                st.balloons()
            except Exception as e:
                st.error(f"⚠️ {e}")
