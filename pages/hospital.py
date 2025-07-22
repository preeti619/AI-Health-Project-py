import streamlit as st
import webbrowser

def show_hospital_page():
    st.subheader("🏥 Nearby Hospital")
    if st.button("Open Google Maps for Nearby Hospitals"):
        webbrowser.open("https://www.google.com/maps/search/nearby+hospitals/")