import streamlit as st
from form import form_buttons as fb, form_fields as ffields, form_functions as ffunctions, form_messages as fm
from config import pagesetup as ps

def get_subform_auth_newuser():
    subform_auth_newuser = st.form(
        key = "subform_auth_newuser",
        border=True
    )
    with subform_auth_newuser:
        username = ffields.formfield_username("new")
        credential = ffields.formfield_credential("new")
        submit = fb.formbutton_submit()
        if submit and username is not None and credential is not None:
            try:
                new_user = ffunctions.add_new_user(varUsername=username, varCredential=credential)
            except Exception as e:
                new_user_error = fm.get_error_message(varError=e, varType="new")
            else:
                new_user_success = fm.get_success_message(varType="new")
                ffunctions.update_auth_sessionstates(varUsername=username, varCredential=credential)



def get_subform_auth_existinguser():
    subform_auth_existinguser = st.form(
        key = "subform_auth_existinguser",
        border=True
    )
    with subform_auth_existinguser:
        username = ffields.formfield_username("existing")
        credential = ffields.formfield_credential("existing")
        submit = fb.formbutton_submit()
        if submit and username is not None and credential is not None:
            validate_user = ffunctions.check_existing_user(varUsername=username, varCredential=credential)
            if validate_user > 0:
                existing_user_success = fm.get_success_message("existing")
                ffunctions.update_auth_sessionstates(varUsername=username, varCredential=credential)
            else:
                existing_user_error = fm.get_error_message(varType="existing", varError=st.secrets.loginform.login_error_message)

def get_subform_auth():
    auth_container = st.container(border=True)
    with auth_container:
        tab1, tab2 = st.tabs(tabs=["New User", "Existing User"])
        with tab1: 
            get_subform_auth_newuser()
        with tab2:
            get_subform_auth_existinguser()


def get_subform_terms_acknowledged():
    
    subform_terms_acknowledged = st.form(
        key = "subform_terms_acknowledged",
        border=True
    )
    with subform_terms_acknowledged:
        terms_container = st.container(border=True, height=200)
        with terms_container:
            terms_content = st.markdown(fm.get_terms_conditions_content())
        acknowledge = ffields.formfield_acknowledge()
        submit = fb.formbutton_submit()
        if submit and acknowledge:
            terms_success = fm.get_success_message("terms")
            ffunctions.update_terms_sessionstates(varAcknowledged=acknowledge)
        else:
            terms_error = fm.get_error_message(varType="terms", varError=st.secrets.termsform.message_error_terms)


def get_subform_about():
    about_container = st.container()
    with about_container:
        content = st.markdown(fm.get_about_content())

def get_subform_check():
    check_container = st.container()
    with check_container:
        auth_check = ffields.formfield_check_auth()
        terms_check = ffields.formfield_check_terms()
        btnenter = st.button(label="Enter DaddyBets", key="btnEnter")
        if btnenter:
            ffunctions.update_validated_sessionstates()
            validated = st.session_state.validated
            if validated:
                st.rerun()
            else:
                st.error("Please check again")
            