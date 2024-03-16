import streamlit as st
from form import form_subforms as fs
from config import pagesetup as ps

def set_page_view(varPage):
    st.session_state.wizard_current_step = 1
    st.session_state.wizard_queued_file = None
    st.session_state.wizard_current_view = varPage

def set_form_step(varAction, varStep=None):
    if varAction == "next":
        st.session_state.wizard_current_step = st.session_state.wizard_current_step + 1
    if varAction == "back":
        st.session_state.wizard_current_step = st.session_state.wizard_current_step - 1
    if varAction == "jump":
        st.session_state.wizard_current_step = varStep

def wizard_form_header():
    title_container = st.container(border=False, height=25)
    with title_container:
        ps.set_gray_header('Welcome to DaddyBets!')
    button_container = st.container(border=False, height=20)
    with button_container:
        # determines button color which should be red when user is on that given step
        about_type = 'primary' if st.session_state.wizard_current_view =="about"  else 'secondary'
        terms_type = 'primary' if st.session_state.wizard_current_view ==  "terms" else 'secondary'
        auth_type = 'primary' if st.session_state.wizard_current_view ==  "auth" else 'secondary'
        check_type = 'primary' if st.session_state.wizard_current_view == "check" else 'secondary'
        button_cc = st.columns([1,2,2,2,2,1])
        with button_cc[1]:
            st.button('About',on_click=set_page_view,args=['about'],type=about_type, use_container_width=True)
        with button_cc[2]:
            st.button('Terms and Conditions',on_click=set_page_view,args=['terms'],type=terms_type, use_container_width=True)        
        with button_cc[3]:
            st.button('Authentication',on_click=set_page_view,args=['auth'],type=auth_type, use_container_width=True)      
        with button_cc[4]:
            st.button('Final Check',on_click=set_page_view,args=['check'],type=check_type, use_container_width=True)


def wizard_form_body():
    current_step = st.session_state.wizard_current_step
    current_view = st.session_state.wizard_current_view
    if current_view == "about":
        fs.get_subform_about()
    if current_view == "terms":
        fs.get_subform_terms_acknowledged()
    if current_view == "auth":
        fs.get_subform_auth()
    if current_view == "check":
        fs.get_subform_check()

  
def wizard_form_footer():    
    form_footer_container = st.empty()
    with form_footer_container.container():
        
        disable_back_button = True if st.session_state.wizard_current_step == 1 else False
        disable_next_button = True if st.session_state.wizard_current_step == 4 else False
        
        form_footer_cols = st.columns([5,1,1,1.75])
        
        form_footer_cols[0].button('Cancel',on_click=set_page_view,args=['about'])
        form_footer_cols[1].button('Back',on_click=set_form_step,args=['back'],disabled=disable_back_button)
        form_footer_cols[2].button('Next',on_click=set_form_step,args=['next'],disabled=disable_next_button)
    
        
        


def render_wizard_view():
    with st.expander('',expanded=True):
        wizard_form_header()
        st.markdown('---')
        wizard_form_body()
        st.markdown('---')
        wizard_form_footer()
