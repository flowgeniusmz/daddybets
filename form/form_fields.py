import streamlit as st
from form import form_messages as fm

def formfield_credential(varType):
    if varType=="new":
        field_label = st.secrets.loginform.create_password_label
        field_placeholder = st.secrets.loginform.create_password_placeholder
        field_help = st.secrets.loginform.create_password_help
    elif varType == "exist": 
        field_label = st.secrets.loginform.login_password_label
        field_placeholder = st.secrets.loginform.login_password_placeholder
        field_help = st.secrets.loginform.login_password_help
    
    
    credential_field = st.text_input(
        label=st.secrets.loginform.create_password_label,
        placeholder=st.secrets.loginform.create_password_placeholder,
        help=st.secrets.loginform.create_password_help,
        type="password",
        disabled=st.session_state.authenticated
    )
    return credential_field


def formfield_username(varType):
    if varType=="new":
        field_label = st.secrets.loginform.create_username_label
        field_placeholder = st.secrets.loginform.create_username_placeholder
        field_help = st.secrets.loginform.create_username_help
    elif varType == "exist" or varType == "existing": 
        field_label = st.secrets.loginform.login_username_label
        field_placeholder = st.secrets.loginform.login_username_placeholder
        field_help = st.secrets.loginform.login_username_help
    
    username_field = st.text_input(
        label=field_label,
        placeholder=field_placeholder,
        help=field_help,
        disabled=st.session_state.authenticated
    )
    return username_field

def formfield_acknowledge():
    display_state = st.session_state.acknowledged
    check_acknowledge = st.checkbox(
        label=st.secrets.termsform.label_checkbox_acknowledge,
        value=display_state,
        key="formfield_checkbox_acknowledge",
        help=st.secrets.termsform.help_checkbox_acknowledge
    )
    return check_acknowledge

def formfield_check_auth():
    display_state = st.session_state.authenticated
    cc = st.columns([1,5])
    with cc[0]:
        check_auth = st.checkbox(
            label="Authentication Complete?",
            value=display_state, 
            disabled=True
        )
    with cc[1]:
        if display_state:
            auth_success = st.success(body="Completed", icon=st.secrets.streamlit.message_icon_success)
        if not display_state:
            auth_error = st.error(body="Incomplete", icon=st.secrets.streamlit.message_icon_error)

def formfield_check_terms():
    display_state = st.session_state.acknowledged
    cc = st.columns([1,5])
    with cc[0]:
        check_terms = st.checkbox(
            label="Terms and Conditions Accepted?",
            value=display_state, 
            disabled=True
        )
    with cc[1]:
        if display_state:
            terms_success = st.success(body="Completed", icon=st.secrets.streamlit.message_icon_success)
        if not display_state:
            terms_error = st.error(body="Incomplete", icon=st.secrets.streamlit.message_icon_error)