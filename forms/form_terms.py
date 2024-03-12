import streamlit as st
from functions import read_file as rf

def get_terms_content():
    file_path_relative = st.secrets.streamlit.terms_and_conditions_realtive_path
    file_path = st.secrets.streamlit.terms_and_conditions_path
    terms = rf.read_get_file(varPath=file_path_relative)
    return terms
