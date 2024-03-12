import streamlit as st

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
    elif varType == "exist": 
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

