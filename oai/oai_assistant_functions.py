import streamlit as st
from openai import OpenAI


client = OpenAI(api_key=st.secrets.openai.api_key)



def create_oai_message(varRole, varContent):
    new_message = client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        content=varContent,
        role=varRole
    )
    return new_message

def create_oai_run():
    new_run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=st.secrets.openai.assistant_id,
        additional_instructions=st.session_state.run_instructions
    )
    return new_run

def check_oai_run():
    run_check = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_id,
            run_id=st.session_state.run.id
        )
    return run_check

def get_thread_messages():
    thread_messages = client.beta.threads.messages.list(
        thread_id=st.session_state.thread_id
    )
    return thread_messages
