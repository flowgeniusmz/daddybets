import streamlit as st
from langchain.prompts import PromptTemplate

def get_prompt_betting(varSelectedSport: str, varSelectedRegion: str, varSelectedDate: str):
    input_variables = ["varSelectedSport", "varSelectedRegion", "varSelectedDate"]
    template = "Key Information: 1. Sport = {varSelectedSport}, 2. Region = {varSelectedRegion}, 3. Betting Date = {varSelectedDate}"    
    prompt_template = PromptTemplate(
        input_variables=input_variables,
        template=template
    )
    prompt_betting = prompt_template.format(varSelectedSport=varSelectedSport, varSelectedRegion=varSelectedRegion, varSelectedDate=varSelectedDate)
    
    st.session_state.betting_sport = varSelectedSport
    st.session_state.betting_region = varSelectedRegion
    st.session_state.betting_date = varSelectedDate
    
    return prompt_betting
