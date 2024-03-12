import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from status.chatstatus import Status
from openai import OpenAI
from forms import form_betting as fb
from app import app_bettingassistant as appBA

# 0. Set Master Page Config (see config/pagesetup.py)
ps.master_page_config(1)

# 1. Check and/or Initialize Session States (see config/sessionstates.py)
ss.master_session_state()

# 2. Call App
appBA.get_app_bettingassistant()

# 5. Chat
main_container = st.container(border=True, height=600)
with main_container:
    cc_colwidth = [3,1]
    cc = st.columns(cc_colwidth)
    with cc[0]:
        chat_container = st.container(border=True, height=550)
        with chat_container:
            ps.set_gray_header("Daddy Chat")
    with cc[1]:
        status_container = st.container(border=True, height=550)
        with status_container:
            ps.set_gray_header("Chat Status")

# 6. Display existing messages
with chat_container:
    for existing_message in st.session_state.messages:
        existing_message_role = existing_message["role"]
        existing_message_content = existing_message["content"]
        with st.chat_message(name=existing_message_role):
            st.markdown(body=existing_message_content)