# signup.py
import streamlit as st
from utils.db_helper import add_user

def show_signup():
    st.title("📝 Create Your AI Health Assistant Account")

    username = st.text_input("👤 Username")
    full_name = st.text_input("🧾 Full Name")

    phone = st.text_input("📱 Phone Number")
    email = st.text_input("📧 Email Address")

    password = st.text_input("🔐 Password", type="password")
    confirm_password = st.text_input("🔐 Confirm Password", type="password")
    
    address = st.text_area("🏠 Address")

    if st.button("✅ Sign Up"):
        if not all([username, full_name, phone, email, password, confirm_password, address]):
            st.warning("⚠️ Please fill in all the fields.")
        elif password != confirm_password:
            st.warning("❌ Passwords do not match.")
        else:
            try:
                add_user(username, full_name, phone, email, password, address)
                st.success("🎉 Account created successfully! Proceed to login.")
                st.balloons()
            except:
                st.error("⚠️ Username or email already exists. Try again.")
