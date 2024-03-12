import streamlit as st
import datetime
from config import pagesetup as ps
from functions import get_prompts as prmt
from classes import class_dksports as cs, class_dkteams as ct, class_dkregions as cr

def get_form_betting():
    form_betting_caption = "Please fill out the information below before chatting with Daddy!"
    placeholder_text = "Please choose an option..."
    min_date = datetime.date.today()
    select_sport_label = "Select a Sport"
    select_region_label = "Select a Region"
    select_date_label = "Select Betting Date"
    form_expander = st.expander(label="Expand/Collpase", expanded=st.session_state.betting_form_expander_state)
    form_betting = st.form(key="form_betting", clear_on_submit=False, border=True)
    with form_betting:
        form_betting_columns = st.columns(3)
        with form_betting_columns[0]:
            user_selected_sport = st.selectbox(label=select_sport_label, key="user_selected_sport", options=[sport.value for sport in cs.Sport])
        with form_betting_columns[1]:
            user_selected_region = st.selectbox(label=select_region_label, key="user_selected_region", options=[region.value for region in cr.Region])
        with form_betting_columns[2]:
            user_selected_date = st.date_input(label=select_date_label, key="user_selected_date")
        form_betting_submit_button = st.form_submit_button(label="Submitbet", type="primary")
        if form_betting_submit_button:
            if user_selected_sport is not None and user_selected_region is not None and user_selected_date is not None:
                betting_prompt = prmt.get_prompt_betting(varSelectedSport=user_selected_sport, varSelectedDate=user_selected_date, varSelectedRegion=user_selected_region)
                sport_object = get_dk_info(varSelectedSport=user_selected_sport)
                st.session_state.betting_prompt = betting_prompt
                st.session_state.betting_form_expander_state = False
                st.markdown(betting_prompt)
                st.markdown(sport_object)
            else:
                if user_selected_sport is None:
                    st.warning(body="**ERROR**: Please select a sport.", icon="⚠️")
                if user_selected_region is None:
                    st.warning(body="**ERROR**: Please select a region.", icon="⚠️")
                if user_selected_date is None:
                    st.warning(body="**ERROR**: Please enter a date.", icon="⚠️")


def append_to_sport_object(varSport, varEventGroupId, varSportId, varSportName):
    new_row = {
        "selectedsport": varSport,
        "eventgroupid": varEventGroupId,
        "sportid": varSportId,
        "name": varSportName
    }
    st.session_state.betting_object_sports = new_row
    return new_row


def get_dk_info(varSelectedSport):
    sport = st.session_state.user_selected_sport
    sport_eventgroupid, sport_id, sport_name = cs.get_sport_details(user_selected_sport_label=sport)
    sport_object = append_to_sport_object(varSport=sport, varEventGroupId=sport_eventgroupid, varSportId=sport_id, varSportName=sport_name)
    return sport_object



   