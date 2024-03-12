import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from form import form_wizard as fw

ps.get_st_page_config()
# 0. Set Master Page Config (see config/pagesetup.py)
ps.master_page_config(0)


# 1. Check and/or Initialize Session States (see config/sessionstates.py)
ss.master_session_state()

if not st.session_state.validated:
    fw.render_wizard_view()
else:

    # 2. Page Link Section
    promo_container = st.container(height=200)
    with promo_container:
        st.markdown("Promo")
    st.divider()
    ps.page_links_section()