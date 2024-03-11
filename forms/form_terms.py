import streamlit as st
from config import pagesetup as ps
from forms import form_login as fl


def read_get_file(varPath):
    with open(varPath, "r") as file:
        file_path_content = file.read()
        return file_path_content

def get_success_message():
    terms_success = st.success(
        body="SUCCESS: Terms and conditions have been successfully accepted. Please continue to login.",
        icon="✅"
    )

def get_error_message():
    terms_error = st.error(
        body="ERROR: Please acknowledge the Terms and Conditions by checking the box.",
        icon="⚠️"
    )
def get_terms_content():
    file_path_relative = st.secrets.streamlit.terms_and_conditions_realtive_path
    file_path = st.secrets.streamlit.terms_and_conditions_path
    terms_file = open(file=file_path, mode="r")
    terms_file_content = terms_file.read()
    return terms_file_content

def formfield_acceptterms():
    acceptterms_formfield = st.checkbox(
        label="I have read and acknowledge the DaddyBets Terms and Conditions",
        value=st.session_state.user_accepted_terms_checkbox, 
        key="checkbox_terms"
    )
    return acceptterms_formfield

def formbutton_acknowledge():
    acknowledge_formbutton = st.form_submit_button(
        label="Acknowledge Terms",
        help="You must acknowledge the DaddyBets Terms and Conditions prior to entering the site."
    )

def subform_terms():    
    subform_terms = st.form(key="subform_login")
    with subform_terms:
        subform_terms_accepted = formfield_acceptterms()
        subform_terms_button = formbutton_acknowledge()
        if subform_terms_button:
            if subform_terms_accepted:
                st.session_state.acknowledged = True
                get_success_message()
            else:
                st.session_state.acknowledged = False
                get_error_message()
def get_terms_expander():
    terms_expander_label = st.secrets.termsform.title
    terms_expander_expanded = not st.session_state.acknowledged
    terms_expander = st.expander(
        label=terms_expander_label,
        expanded=terms_expander_expanded
    )
    with terms_expander:
        subform_terms()
    
def get_terms_form():
    terms_container = st.container(border=True, height=400)
    with terms_container:
        ps.get_blue_header("Terms and Conditions")
        st.caption(body="You must accept the terms at the bottom of this form.")
        get_terms_expander()