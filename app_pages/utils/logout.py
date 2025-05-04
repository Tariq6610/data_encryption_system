import streamlit as st

def logout():
    st.query_params = {"page" : "signIn"}
    st.rerun()