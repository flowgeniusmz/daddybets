import streamlit as st
from forms import form_betting as fb
from config import pagesetup as ps
from status import chatstatus as cs
from oai import oai_assistant_functions as asstfun



def display_existing_chat_messages():
    msgs = st.session_state.messages
    for msg in msgs:
        msg_role = msg["role"]
        msg_content = msg["content"]
        with st.chat_message(name=msg_role):
            st.markdown(msg_content)



def get_subapp_bettingassistant_selection():
    selection_form = fb.get_form_betting()

def get_subapp_bettingassistant_assistant():
    assistant_container_columns = st.columns([3,1])
    with assistant_container_columns[0]:
        ps.set_gray_header("Daddy Chat")
        chat_container = st.container(border=True, height=550)
        with chat_container:
            display_existing_chat_messages() # function
    with assistant_container_columns[1]:
        ps.set_gray_header("Status")
        status_container = st.container(border=True, height=550)

def get_app_bettingassistant():
    selection_container = st.container(border=True, height=200)
    with selection_container:
        get_subapp_bettingassistant_selection()
    
    assistant_container = st.container(border=True, height=600)
    with assistant_container:
        get_subapp_bettingassistant_assistant()
