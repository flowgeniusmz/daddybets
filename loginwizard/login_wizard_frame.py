import streamlit as st
from forms import form_login as fl, form_terms as ft
from config import pagesetup as ps
from sessionstates import sessionstates_wizard as sswiz


def set_page_view(varPage):
    st.session_state.wizard_current_view = varPage
    st.session_state.wizard_current_step = 1

def set_form_step(varAction, varStep=None):
    if varAction == "Next": 
        st.session_state.wizard_current_step = st.session_state.wizard_current_step + 1
    if varAction == "Back":
        st.session_state.wizard_current_step = st.session_state.wizard_current_step -  1
    if varAction == "Jump":
        st.session_state.wizard_current_step = varStep 

##### wizard functions ####
def wizard_button_types(varType):
    about_type = "primary" if st.session_state.wizard_current_step == 1 else "secondary"
    terms_type = "primary" if st.session_state.wizard_current_step == 2 else "secondary"
    auth_type = "primary" if st.session_state.wizard_current_step == 3 else "secondary"
    submit_type = "primary" if st.session_state.wizard_current_step == 4 else "secondary"

    if varType == "about":
        response_type =  about_type
    elif varType == "terms":
        response_type = terms_type
    elif varType == "auth":
        response_type = auth_type
    elif varType == "submit":
        response_type = submit_type

    return response_type

def wizard_step_cols():
    # determines button color which should be red when user is on that given step
    btn_about_type = wizard_button_types("about")
    btn_terms_type = wizard_button_types("terms")
    btn_auth_type = wizard_button_types("auth")
    btn_submit_type = wizard_button_types("submit")

    step_cols = st.columns([.5,.85,.85,.85,.85,.5])    
    with step_cols[1]:
        step_button_about = st.button(
            label=st.secrets.wizardform.button_label_about,
            on_click=set_form_step,
            args=['Jump',1],
            type=btn_about_type
            )
    with step_cols[2]:
        step_button_terms = st.button(
            label=st.secrets.wizardform.button_label_terms,
            on_click=set_form_step,
            args=['Jump',2],
            type=btn_terms_type
            )      
    with step_cols[3]:
        step_button_auth = st.button(
            label=st.secrets.wizardform.button_label_auth,
            on_click=set_form_step,
            args=['Jump',3],
            type=btn_auth_type
            )
    with step_cols[4]:
        step_button_submit = st.button(
            label=st.secrets.wizardform.button_label_submit,
            on_click=set_form_step,
            args=['Jump',4],
            type=btn_submit_type
            )
        
def button_state_back_next(varType):
    if varType == "next":
        button_state = True if st.session_state.wizard_current_step == 1 else False
    elif varType == "back":
        button_state = True if st.session_state.wizard_current_step == 4 else False
    elif varType == "file":
        False if st.session_state.wizard_queued_file is not None else True
    return button_state


def wizard_form_header():
    header_cols = st.columns([1,1.75,1])
    with header_cols[1]:
        wizard_header = st.subheader(body=st.secrets.wizardform.header)
    wizard_step_cols()

def wizard_form_body():
    st.write(st.session_state['current_step'])   

def wizard_form_footer():
    form_footer_container = st.empty()
    with form_footer_container.container():
        disable_back_button = button_state_back_next("back")
        disable_next_button = button_state_back_next("next")
        disable_file_ready_button = button_state_back_next("file")
        form_footer_cols = st.columns([5,1,1,1.75])
        with form_footer_cols[0]:
            btn_cancel = st.button(
                label='Cancel',
                on_click=set_page_view,
                args=['Grid']
                )
        with form_footer_cols[1]:
            btn_back = st.button(
                label='Back',
                on_click=set_form_step,
                args=['Back'],
                disabled=disable_back_button
                )
        with form_footer_cols[2]:
            btn_next = st.button(
                label='Next',
                on_click=set_form_step,
                args=['Next'],
                disabled=disable_next_button
                )
    
        file_ready = False if st.session_state['queued_file'] is not None else True
        with form_footer_cols[3]:
            btn_load_file = st.button(
                label = st.secrets.button_load_file_label,
                disabled=disable_file_ready_button
                ) 


### Replace Render Wizard View With This ###
def render_wizard_view():
    with st.expander('',expanded=True):
        wizard_form_header()
        st.markdown('---')
        wizard_form_body()
        st.markdown('---')
        wizard_form_footer()



acknowledged = st.session_state.acknowledged
authenticated = st.session_state.authenticated

def master_login_terms_form():
    master_container = st.container(border=True)
    ps.get_blue_header("Welcome to DaddyBets")
    with master_container:
        mastercc = st.columns(2)
        with mastercc[0]:
            ps.set_gray_header("Terms and Conditions")
            terms_container = st.container(border=True, height=500)
            with terms_container:
                if acknowledged:
                    st.success("Good")
                else:
                    ft.get_terms_form()
        with mastercc[1]:
            ps.set_gray_header("Authentication")
            login_container = st.container(border=True, height=500)
            with login_container:
                if authenticated:
                    st.success("Good")
                else:
                    fl.get_form_login
  