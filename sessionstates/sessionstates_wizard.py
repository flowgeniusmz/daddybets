import streamlit as st

def get_sessionstates_wizard():
    if "wizard_current_step" not in st.session_state:
        st.session_state.wizard_current_step = 1
    if "wizard_current_view" not in st.session_state:
        st.session_state.wizard_current_view = 'about'
    if "wizard_queued_file" not in st.session_state:
        st.session_state.wizard_queued_file = 1
    if "display_master_wizard" not in st.session_state:
        st.session_state.display_master_wizard = True
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "acknowledged" not in st.session_state:
        st.session_state.acknowledged = False
    if "validated" not in st.session_state:
        st.session_state.validated = False
    if "username" not in st.session_state:
        st.session_state.username = None
    if "credential" not in st.session_state:
        st.session_state.credential = None
    