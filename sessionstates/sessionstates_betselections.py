import streamlit as st

def get_sessionstates_betselection():
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
    if "betting_object_sports" not in st.session_state:
        st.session_state.betting_object_sports = {"selectedsport": None, "eventgroupid": None, "sportid": None, "name": None}