import streamlit as st


def open_tab(local_url):
    script_local = f"window.open('{local_url}');"
    return script_local

def warning():
    message = st.write("<span style='color:red'>Please enter a word</span>", unsafe_allow_html=True)
    return message