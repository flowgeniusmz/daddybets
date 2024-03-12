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
    return "a"


def get_subform_auth_existinguser():
    subform_auth_existinguser = st.form(
        key = "subform_auth_existinguser",
        border=True
    )
    with subform_auth_existinguser:
        username = ffields.formfield_username("existing")
        credential = ffields.formfield_credential("existing")
        submit = fb.formbutton_submit()
    return "A"

def get_subform_terms_acknowledged():
    subform_terms_acknowledged = st.form(
        key = "subform_terms_acknowledged",
        border=True
    )
    return "AA"

