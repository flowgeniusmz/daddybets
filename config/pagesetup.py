import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def get_st_page_config():
    st.set_page_config(
        page_title=st.secrets.streamlit.config_app_name,
        page_icon=st.secrets.streamlit.config_app_icon,
        layout=st.secrets.streamlit.config_app_layout,
        initial_sidebar_state=st.secrets.streamlit.config_app_initial_sidebar
        )
# 0. IMAGES
def display_background_image():
    # Set the Streamlit image for branding as the background with transparency
    background_image = 'https://storage.googleapis.com/production-domaincom-v1-0-8/048/1724048/4RBifvGs/dfc737c8f0d640cfa7e8623583bfcf5e'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.90)), url({background_image});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

### TITLES
def get_title_styled(varTitle, varSubtitle):
    with stylable_container(
        key="container_with_border",
        css_styles=["""
            {
                border: 1px solid rgba(115, 0, 0, 1);
                background-color: rgba(115, 0, 0, .75);
            }
            """,
            """
            .stMarkdown {
                    padding-right: .2em;
                    padding-left: .5em;
                """]
        ):
        st.markdown(f"""<span style="font-weight: bold; color:#0096D7; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)
        st.divider()


def get_title_nodiv_styled(varTitle, varSubtitle):
    with stylable_container(
            key="markdown_text",
            css_styles="""
            {
                    background-color: #2b16d7;
                    border-radius: 1em;
                    padding: .75em;
            }
            """,
    ):
        st.markdown(f"""<span style="font-weight: bold; color:#0096D7; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)


### 2.  Wording
def set_blue_header(varSubtitle):
        with stylable_container(
                key="markdown_text",
                css_styles="""
                {
                        background-color: #2b16d7;
                        border-radius: 1em;
                        padding: .75em;
                }
                """,
        ):
            st.markdown(f"""<span style="font-weight: bold; color:#0096D7; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)
    

def set_green_header(varSubtitle):
            st.markdown(f"""<span style="font-weight: bold; color:#00b084; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)

             
### PAGE LINKS ####

def get_pagelinks():

    container_pagelinks = st.container()
    with container_pagelinks:
        st.page_link("Home.py", label="Home", icon="🌐")
        st.page_link("pages/1_Page1.py", label="AI Assistant", icon="🌐")
        st.page_link("pages/2_Page2.py", label="Page 2", icon="🌐")

### 3. PAGE OVERVIEW
def set_page_overview(varHeader, varText):
        with stylable_container(
                key="markdown_text",
                css_styles="""
                {
                        border-color: 1px solid rgba(115,0,0, .7em);
                        background-color: #d75e00;
                        border-radius: 1em;
                        padding: .75em;
                }
                """,
        ):
                set_blue_header(varHeader)
                st.markdown(f"{varText}")
                st.divider()

### 3. PAGE SECTION
def set_page_section(varHeader, varText):
        set_blue_header(varHeader)
        st.markdown(f"{varText}")
        section_placeholder = st.empty()
        st.divider()
        return section_placeholder




# 1. St.Set_Page_Config

    
# 2. Set Title
def get_title(varPageNumber):
    if varPageNumber == 0:
        varTitle = st.secrets.streamlit.config_home_title
        varSubtitle = st.secrets.streamlit.config_home_subtitle
    elif varPageNumber == 1:
        varTitle = st.secrets.streamlit.config_page_title_1
        varSubtitle = st.secrets.streamlit.config_page_subtitle_1
    elif varPageNumber == 2:
        varTitle = st.secrets.streamlit.config_page_title_2
        varSubtitle = st.secrets.streamlit.config_page_subtitle_2
    elif varPageNumber == 3:
        varTitle = st.secrets.streamlit.config_page_title_3
        varSubtitle = st.secrets.streamlit.config_page_subtitle_3
    elif varPageNumber == 4:
        varTitle = st.secrets.streamlit.config_page_title_4
        varSubtitle = st.secrets.streamlit.config_page_subtitle_4
    else:
        varTitle = st.secrets.streamlit.config_home_title
        varSubtitle = st.secrets.streamlit.config_home_subtitle

    st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#4A90E2;">{varTitle} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)
    st.divider()

def get_title_no_divider(varPageNumber):
    if varPageNumber == 0:
        varTitle = st.secrets.streamlit.config_home_title
        varSubtitle = st.secrets.streamlit.config_home_subtitle
    elif varPageNumber == 1:
        varTitle = st.secrets.streamlit.config_page_title_1
        varSubtitle = st.secrets.streamlit.config_page_subtitle_1
    elif varPageNumber == 2:
        varTitle = st.secrets.streamlit.config_page_title_2
        varSubtitle = st.secrets.streamlit.config_page_subtitle_2
    elif varPageNumber == 3:
        varTitle = st.secrets.streamlit.config_page_title_3
        varSubtitle = st.secrets.streamlit.config_page_subtitle_3
    elif varPageNumber == 4:
        varTitle = st.secrets.streamlit.config_page_title_4
        varSubtitle = st.secrets.streamlit.config_page_subtitle_4
    else:
        varTitle = st.secrets.streamlit.config_home_title
        varSubtitle = st.secrets.streamlit.config_home_subtitle

    st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#4A90E2;">{varTitle} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)
    
# 3. Get Overview
def get_overview(varPageNumber):
    if varPageNumber == 0:
        varOverviewHeader = st.secrets.streamlit.config_home_overview_header
        varPageDescription = st.secrets.streamlit.config_home_description
        varSubtitle = st.secrets.streamlit.config_home_subtitle
    elif varPageNumber == 1:
        varOverviewHeader = st.secrets.streamlit.config_page_overview_header_1
        varPageDescription = st.secrets.streamlit.config_page_description_1
        varSubtitle = st.secrets.streamlit.config_page_subtitle_1
    elif varPageNumber == 2:
        varOverviewHeader = st.secrets.streamlit.config_page_overview_header_2
        varPageDescription = st.secrets.streamlit.config_page_description_2
        varSubtitle = st.secrets.streamlit.config_page_subtitle_2
    elif varPageNumber == 3:
        varOverviewHeader = st.secrets.streamlit.config_page_overview_header_3
        varPageDescription = st.secrets.streamlit.config_page_description_3
        varSubtitle = st.secrets.streamlit.config_page_subtitle_3
    elif varPageNumber == 4:
        varOverviewHeader = st.secrets.streamlit.config_page_overview_header_4
        varPageDescription = st.secrets.streamlit.config_page_description_4
        varSubtitle = st.secrets.streamlit.config_page_subtitle_4
    else:
        varOverviewHeader = st.secrets.streamlit.config_home_overview_header
        varPageDescription = st.secrets.streamlit.config_home_description
        varSubtitle = st.secrets.streamlit.config_home_subtitle

    st.markdown(f"""<span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{varOverviewHeader}</span>""", unsafe_allow_html=True)    
    st.markdown(f"**{varSubtitle}** {varPageDescription.lower()}")
    st.divider()

# 4. Set Headers
def get_blue_header(varText):
    st.markdown(f"""<span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)    

def set_gray_header(varText):
    st.markdown(f"""<span style="font-weight: bold; color:#333333; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)

# 5. Set Deans Assistant Title
def get_deans_assistant_title(varPageNumber):
    title_container = st.container()
    with title_container:
        title_columns = st.columns(2)
        with title_columns[0]:
            get_title_no_divider(varPageNumber=varPageNumber)
        with title_columns[1]:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQroYsyWjvZmkyguxf2_XUKqcWTNLkZrRbPzPL8MU5I&s', caption='Plainfield School District 202') #Streamlit image for branding
        st.divider()

# 6. Page Links
def get_page_link(varPageNumber):
    if varPageNumber == 0:
        varPagePath = st.secrets.streamlit.config_home_path
        varPageIcon = st.secrets.streamlit.config_home_icon
        varPageSubtitle = st.secrets.streamlit.config_home_subtitle
        varPageLinkAbout = st.secrets.streamlit.config_page_home_link_about
    elif varPageNumber == 1:
        varPagePath = st.secrets.streamlit.config_page_path_1
        varPageIcon = st.secrets.streamlit.config_page_icon_1
        varPageSubtitle = st.secrets.streamlit.config_page_subtitle_1
        varPageLinkAbout = st.secrets.streamlit.config_page_page_link_about_1
    elif varPageNumber == 2:
        varPagePath = st.secrets.streamlit.config_page_path_2
        varPageIcon = st.secrets.streamlit.config_page_icon_2
        varPageSubtitle = st.secrets.streamlit.config_page_subtitle_2
        varPageLinkAbout = st.secrets.streamlit.config_page_page_link_about_2
    elif varPageNumber == 3:
        varPagePath = st.secrets.streamlit.config_page_path_3
        varPageIcon = st.secrets.streamlit.config_page_icon_3
        varPageSubtitle = st.secrets.streamlit.config_page_subtitle_3
        varPageLinkAbout = st.secrets.streamlit.config_page_page_link_about_3
    elif varPageNumber == 4:
        varPagePath = st.secrets.streamlit.config_page_path_4
        varPageIcon = st.secrets.streamlit.config_page_icon_4
        varPageSubtitle = st.secrets.streamlit.config_page_subtitle_4
        varPageLinkAbout = st.secrets.streamlit.config_page_page_link_about_4
    else:
        varPagePath = st.secrets.streamlit.config_home_path
        varPageIcon = st.secrets.streamlit.config_home_icon
        varPageSubtitle = st.secrets.streamlit.config_home_subtitle
        varPageLinkAbout = st.secrets.streamlit.config_page_home_link_about

    page_link_container = st.container(border=True)
    with page_link_container:
        page_link = st.page_link(
            page=varPagePath,
            label=varPageSubtitle,
            icon=varPageIcon
        )
        page_link_about = st.expander(label="About", expanded=False)
        with page_link_about:
            st.markdown(varPageLinkAbout)




def get_page_styling():
    with open("config/style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
        

def master_page_config(varPageNumber):
    #get_st_page_config()
    display_background_image()
    get_page_styling()
    get_title(varPageNumber=varPageNumber)
    get_overview(varPageNumber=varPageNumber)


def page_links_section():
    link_container = st.container(border=True)
    with link_container:
        link_columns = st.columns(2)
        with link_columns[0]:
            get_page_link(1)
            get_page_link(3)
        with link_columns[1]:
            get_page_link(2)
            get_page_link(4)
         