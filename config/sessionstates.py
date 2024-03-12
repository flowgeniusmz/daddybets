import streamlit as st
import uuid
from openai import OpenAI
import pandas as pd
from datetime import datetime
import time
from dataframes import dataframe_create as dfCreate
from status.chatstatus import initialize_status

### ALL SESSION STATES 

def get_initial_session_states():
    if "initalized" not in st.session_state:
        st.session_state.initialized = True
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "acknowledged" not in st.session_state:
        st.session_state.acknowledged = False
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    if "start_datetime" not in st.session_state:
        st.session_state.start_datetime = datetime.now()
        st.session_state.start_unixtime = int(time.mktime(st.session_state.start_datetime.timetuple()))
    if "school_name" not in st.session_state:
        st.session_state.school_name = "John F Kennedy Middle School"
        st.session_state.initial_message = {"role": "assistant", "content": f"Daddy is here! Ask away and watch Daddy cook!", "messageid": "0", "runid": "0", "createdatunix": st.session_state.start_unixtime, "createdatdatetime": st.session_state.start_datetime}
    if "openai_client" not in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=st.secrets.openai.api_key)
        st.session_state.openai_model = st.secrets.openai.model_gpt4_preview
    if "assistant" not in st.session_state:
        st.session_state.assistant = st.session_state.openai_client.beta.assistants.retrieve(assistant_id=st.secrets.openai.assistant_id)
        st.session_state.assistant_instructions = st.session_state.assistant.instructions
        st.session_state.assistant_file_ids = st.session_state.assistant.file_ids
        st.session_state.assistant_tools = st.session_state.assistant.tools
        st.session_state.assistant_model = st.session_state.assistant.model
        st.session_state.assistant_name = st.session_state.assistant.name
        st.session_state.assistant_description = st.session_state.assistant.description
    if "thread" not in st.session_state:
        st.session_state.thread = st.session_state.openai_client.beta.threads.create(
            metadata={'session_id': st.session_state.session_id,}
        )
        st.session_state.thread_id = st.session_state.thread.id
    if "start_chat" not in st.session_state:
        st.session_state.start_chat = True
    if "start_manage" not in st.session_state:
        st.session_state.start_manage = False
    if "file_id_list" not in st.session_state:
        st.session_state.file_id_list = []
    if "ignore_file_ids" not in st.session_state:
        st.session_state.ignore_file_ids = True
    if "run" not in st.session_state:
        st.session_state.run = {"status": None}
        st.session_state.run_instructions = "Ensure you review all your instructions and documents you have been provided. Ensure you follow the process. Ensure you perform your simulations. Ensure you return the types of bets being requested."
    if "messages" not in st.session_state:
        st.session_state.messages = [st.session_state.initial_message]
    if "retry_error" not in st.session_state:
        st.session_state.retry_error = 0
    if "dataframe_files" not in st.session_state:
        #st.session_state.dataframe_files = pd.DataFrame(columns=["File Id", "Object Type", "Created At", "Assistant Id"])
        st.session_state.dataframe_files = dfCreate.create_dataframe_oai_assistantfiles()
    if "dataframe_files1" not in st.session_state:
        #st.session_state.dataframe_files1 = pd.DataFrame(columns=["Id", "Object", "Bytes", "Created At", "Name", "Purpose", "Download Link"])
        st.session_state.dataframe_files1 = dfCreate.create_dataframe_oai_filedownload()
    if "dataframe_tools" not in st.session_state:
        #st.session_state.dataframe_tools = pd.DataFrame(columns=["Type"])
        st.session_state.dataframe_tools = dfCreate.create_dataframe_oai_assistanttools()
    if "dataframe_messages" not in st.session_state:
        st.session_state.dataframe_messages = pd.DataFrame(columns=["Role", "Content", "Thread Id", "Message Id", "Run Id", "Session Id", "Created At Unix", "Created At Datetime"])
    if "new_row_messages" not in st.session_state:
        st.session_state.new_row_messages = {"Role": None, "Content": None, "Thread Id": None, "Message Id": None, "Run Id": None, "Session Id": None, "Created At Unix": None, "Created At Datetime": None}
    if "new_row_files" not in st.session_state:
        st.session_state.new_row_files = {"File Id": None, "Object Type": None, "Created At": None, "Assistant Id": None}
    if "new_row_files1" not in st.session_state:
        st.session_state.new_row_files1 = {"Id": None, "Object": None, "Bytes": None, "Created At": None, "Name": None, "Purpose": None }
    if "new_row_tools" not in st.session_state:
        st.session_state.new_row_tools = {"Type": None}
    if "input_object" not in st.session_state:
        st.session_state.input_object = {"Sport": None, "BetTypes": None, "UserPrompt": None, "AdditionalInstructions": None, "Hometeam": None, "Awayteam": None, "Homeinjury": None, "Awayinjury": None, "Weather": None}

    if "betting_sport" not in st.session_state:
        st.session_state.betting_sport = None
    if "betting_region" not in st.session_state:
        st.session_state.betting_region = None
    if "betting_date" not in st.session_state:
        st.session_state.betting_date = None
    if "betting_prompt" not in st.session_state:
        st.session_state.betting_prompt = None
    if "dataframe_dk_sports" not in st.session_state:
        st.session_state.dataframe_dk_sports = dfCreate.get_dataframe_dk_sports()
    if "dataframe_dk_regions" not in st.session_state:
        st.session_state.dataframe_dk_regions = dfCreate.get_dataframe_dk_regions()
    if "dataframe_dk_teams" not in st.session_state:
        st.session_state.dataframe_dk_teams = dfCreate.get_dataframe_dk_teams()
    if "dataframe_added_oia_file_list" not in st.session_state:
        st.session_state.dataframe_added_oia_file_list = dfCreate.create_dataframe_added_oai_file_list()
    if "betting_form_expander_state" not in st.session_state:
        st.session_state.betting_form_expander_state = True
    if "weather_status" not in st.session_state:   
        st.session_state.weather_status = initialize_status("weather")
    if "odds_status" not in st.session_state:
        st.session_state.odds_status = initialize_status("odds")
    if "unknown_status" not in st.session_state:
        st.session_state.unknown_status = initialize_status("unknown")
    if "user_accepted_terms" not in st.session_state:
        st.session_state.user_accepted_terms = False
        st.session_state.user_accepted_terms_date = None
        st.session_state.user_accepted_terms_checkbox = False
    if "wizard_current_step" not in st.session_state:
        st.session_state.wizard_current_step = "about"
    if "terms_accedpted" not in st.session_state:
        st.session_state.terms_accepted = False
    if "customer_status" not in st.session_state:
        st.session_state.customer_status = None #'new or returning


#### INDIVIDUAL SESSION STATE FUNCTIONS
def get_session_states_stripe():
    if "terms_accedpted" not in st.session_state:
        st.session_state.terms_accepted = False
    if "customer_status" not in st.session_state:
        st.session_state.customer_status = None #'new or returning

def get_session_states_status():
    if "weather_status" not in st.session_state:   
        st.session_state.weather_status = initialize_status("weather")
    if "odds_status" not in st.session_state:
        st.session_state.odds_status = initialize_status("odds")
    if "unknown_status" not in st.session_state:
        st.session_state.unknown_status = initialize_status("unknown")

def get_session_states_dataframes():
    if "dataframe_dk_sports" not in st.session_state:
        st.session_state.dataframe_dk_sports = dfCreate.get_dataframe_dk_sports()
    if "dataframe_dk_regions" not in st.session_state:
        st.session_state.dataframe_dk_regions = dfCreate.get_dataframe_dk_regions()
    if "dataframe_dk_teams" not in st.session_state:
        st.session_state.dataframe_dk_teams = dfCreate.get_dataframe_dk_teams()    
    if "dataframe_files" not in st.session_state:
        #st.session_state.dataframe_files = pd.DataFrame(columns=["File Id", "Object Type", "Created At", "Assistant Id"])
        st.session_state.dataframe_files = dfCreate.create_dataframe_oai_assistantfiles()
    if "dataframe_files1" not in st.session_state:
        #st.session_state.dataframe_files1 = pd.DataFrame(columns=["Id", "Object", "Bytes", "Created At", "Name", "Purpose", "Download Link"])
        st.session_state.dataframe_files1 = dfCreate.create_dataframe_oai_filedownload()
    if "dataframe_tools" not in st.session_state:
        #st.session_state.dataframe_tools = pd.DataFrame(columns=["Type"])
        st.session_state.dataframe_tools = dfCreate.create_dataframe_oai_assistanttools()
    if "dataframe_messages" not in st.session_state:
        st.session_state.dataframe_messages = pd.DataFrame(columns=["Role", "Content", "Thread Id", "Message Id", "Run Id", "Session Id", "Created At Unix", "Created At Datetime"])
    if "dataframe_added_oia_file_list" not in st.session_state:
        st.session_state.dataframe_added_oia_file_list = dfCreate.create_dataframe_added_oai_file_list()
        
def get_session_states_session():

    if "initalized" not in st.session_state:
        st.session_state.initialized = True
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    if "start_datetime" not in st.session_state:
        st.session_state.start_datetime = datetime.now()
        st.session_state.start_unixtime = int(time.mktime(st.session_state.start_datetime.timetuple()))
    
def get_session_states_authentication():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None
    if "credential" not in st.session_state:
        st.session_state.credential = None
    if "email" not in st.session_state:
        st.session_state.email = None
    if "user_subscribed" not in st.session_state:
        st.session_state.user_subscribed = None
    if "user_date_created" not in st.session_state:
        st.session_state.user_date_created = None
    if "user_last_activity_date" not in st.session_state:
        st.session_state.user_last_activity_date = None
    if "user_betting_region" not in st.session_state:
        st.session_state.user_betting_region = None
        

def get_session_state_betting_form():
    if "betting_sport" not in st.session_state:
        st.session_state.betting_sport = None
    if "betting_region" not in st.session_state:
        st.session_state.betting_region = None
    if "betting_date" not in st.session_state:
        st.session_state.betting_date = None
    if "betting_prompt" not in st.session_state:
        st.session_state.betting_prompt = None

def get_session_state_terms_form():
    if "user_accepted_terms" not in st.session_state:
        st.session_state.user_accepted_terms = False
        st.session_state.user_accepted_terms_date = None

#### SESSION STATE CHECK AND MASTER

        
def session_state_check():
    if "initalized" not in st.session_state:
        return False
    elif not st.session_state.initialized:
        return False
    else: 
        return True


def master_session_state():
    check_session_state = session_state_check()
    if not check_session_state:
        get_initial_session_states()