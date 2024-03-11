import streamlit as st

def get_sessionstates_wizard():
    if "wizard_current_step" not in st.session_state:
        st.session_state.wizard_current_step = 1
    if "wizard_current_view" not in st.session_state:
        st.session_state.wizard_current_view = 'Grid'
    if "wizard_queued_file" not in st.session_state:
        st.session_state.wizard_queued_file = 1
    if "display_master_wizard" not in st.session_state:
        st.session_state.display_master_wizard = True