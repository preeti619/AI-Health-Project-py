import streamlit as st
from utils.gpt_response import ask_gpt
from utils.health_logic import predict_condition
from utils.db_helper import store_chat

def show_chatbot_page():
    st.subheader("💬 Ask a Health Question or Enter Symptoms")

    mode = st.radio("Choose Input Mode:", ["Chat With AI", "Simple Symptoms"], horizontal=True)
    user_input = st.text_area("📝 Please enter your input")

    submit_btn = st.button("Submit", type="primary")

    if submit_btn:
        if not user_input.strip():
            st.warning("⚠️ Please enter something to continue.")
            return

        if mode == "Chat With AI":
            reply = ask_gpt(user_input)
        else:
            symptoms = [s.strip().lower() for s in user_input.split(",")]
            reply = predict_condition(symptoms)

        st.success("🤖 AI: " + reply)

        # Optional: check username exists
        if "username" in st.session_state:
            store_chat(st.session_state.username, user_input, reply)
