import streamlit as st
from config import pagesetup as ps, sessionstates as ss


# 0. Set Master Page Config (see config/pagesetup.py)
ps.master_page_config(0)

# 1. Check and/or Initialize Session States (see config/sessionstates.py)
ss.master_session_state()

# 2. Page Link Section
promo_container = st.container(height=200)
with promo_container:
    st.markdown("Promo")
st.divider()
ps.page_links_section()