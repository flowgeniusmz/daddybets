import streamlit as st
from config import pagesetup as ps

authenticated = st.session_state.authenticated
acknowledged = st.session_state.acknowledged
erroricon = "⚠️"
successicon = "✅"

def display_master_wizard(varAuth, varAck, varSub):
    if varAuth and varAck and varSub:
        display = False
    else:
        display = True
    st.session_state.display_master_wizard = display
    return display

def get_submit_error(varType):
    if varType == "terms":
        error_message = "**INCOMPLETE**: Terms and Conditions have not been accepted. Please review that section again."
    if varType =="auth":
        error_message = "**INCOMPLETE**: Authentication has not been completed. Please ensure you are using the proper login."
    display_error = st.error(
        body=error_message,
        icon=erroricon
    )

def get_submit_success(varType):
    if varType == "terms":
        success_message = "**SUCCESS**: Terms and Conditions have been accepted!"
    if varType =="auth":
        success_message = "**SUCCESS**: Authentication is complete!"
    display_error = st.success(
        body=success_message,
        icon=successicon
    )

def submit_form_button(varAuthenticated, varAcknowledged):
    if varAcknowledged and varAuthenticated:
        submit_form_button_state = True
    else:
        submit_form_button_state = False

    btn_submit_form = st.button(
        label="Submit",
        key="final_wizard_submit_btn",
        on_click=display_master_wizard,
        args=[varAuthenticated, varAcknowledged, btn_submit_form]
    )
       
def submit_form_headers():
    submit_header_cols = st.columns([1,2,1])

def submit_form_body():
    body_cols = st.columns([1,3,1,3,1])
    with body_cols[1]:
        ps.set_gray_header("Terms and Conditions")
        body_terms_container = st.container(border=True, height=275)
        with body_terms_container:
            if acknowledged:
                get_submit_success(varType="terms")
            else:
                get_submit_error(varType="terms")
    with body_cols[3]:
        ps.set_gray_header("Authentication")
        body_auth_container = st.container(border=True, height=275)
        with body_auth_container:
            if authenticated:
                get_submit_success(varType="auth")
            else:
                get_submit_error(varType="auth")

def get_submit_form_footer():
    footer_cols = st.columns([1,3,1])
    with footer_cols[1]:
        final_button = submit_form_button(varAcknowledged=acknowledged, varAuthenticated=authenticated)
        if final_button:
            st.session_state.display_master_wizard = False
            st.rerun()

def get_submit_form():
    authenticated = st.session_state.authenticated
    acknowledged = st.session_state.acknowledged
    submit_container = st.container(border=True)
    with submit_container:
        submit_header_container = st.container(border=True, height = 100)
        with submit_header_container:
            ps.set_blue_header("Submit")
        submit_body_container = st.container(border=True, height = 300)
        with submit_body_container:
            submit_form_body()
        submit_footer_container = st.container(border=True, height = 100)
        with submit_footer_container:
            get_submit_form_footer()
        
        
        submit_bodycontainer_cols = st.columns([1,3,1,3,1])
        with submit_container_cols[1]:
            ps.set_gray_header("Terms and Conditions")
            submit_term_container = st.container(border=True)
        with submit_container_cols[3]:
            ps.set_gray_header("Authentication")
            submit_auth_container = st.container(border=True)
        
        

