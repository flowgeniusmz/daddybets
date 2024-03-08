import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from form.form_login import get_form_login

# 0. Set Master Page Config (see config/pagesetup.py)
ps.master_page_config(0)

# 1. Check and/or Initialize Session States (see config/sessionstates.py)
ss.master_session_state()

# Login
if not st.session_state.authenticated:
    get_form_login()
else:
    # 2. Page Link Section
    ps.page_links_section()