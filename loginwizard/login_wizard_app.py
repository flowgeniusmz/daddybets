import streamlit as st
from forms import form_login as fl, form_terms as ft

def wizard_app_authterms_about():
    st.write("1")

def wizard_app_authterms_terms():
    ft.get_terms_form()

def wizard_app_authterms_auth():
    fl.get_form_login

def wizard_app_authterms_submit():
    st.write("4")

def wizard_form_auth_terms():
    step = st.session_state.wizard_current_step
    if step == "about":
        wizard_app_authterms_about()
    elif step == "terms":
        wizard_app_authterms_terms()
    elif step == "auth":
        wizard_app_authterms_auth()
    elif step == "submit":
        wizard_app_authterms_submit()

