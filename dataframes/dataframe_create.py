import streamlit as st
import pandas as pd
from oai import oai_files as f


def create_dataframe_from_csv(varFilePath):
    created_df = pd.read_csv(
        filepath_or_buffer=varFilePath
    )
    return created_df

@st.cache_data
def get_dataframe_dk_sports():
    filepath = st.secrets.streamlit.data_dk_sportlist_path
    df_dk_sports = create_dataframe_from_csv(varFilePath=filepath)
    return df_dk_sports

@st.cache_data
def get_dataframe_dk_regions():
    filepath = st.secrets.streamlit.data_dk_regionlist_path
    df_dk_region = create_dataframe_from_csv(varFilePath=filepath)
    return df_dk_region

@st.cache_data
def get_dataframe_dk_teams():
    filepath = st.secrets.streamlit.data_dk_teamlist_path
    df_dk_teams = create_dataframe_from_csv(varFilePath=filepath)
    return df_dk_teams


@st.cache_data        
def create_dataframe_oai_filedownload():
    varFileIds = st.session_state.assistant_file_ids
    df_oai_filedownload = pd.DataFrame(
        columns=["Id", "Object", "Bytes", "Created At", "Name", "Purpose", "Download Link"]
    )
    for varFileId in varFileIds:
        file_data = f.retrive_oia_files(varFileId=varFileId)
        df_oai_filedownload = df_oai_filedownload._append(file_data, ignore_index=True)
    return df_oai_filedownload

@st.cache_data
def create_dataframe_oai_assistantfiles():
    varFileIds = st.session_state.assistant_file_ids
    df_oai_assistantfiles = pd.DataFrame(
        columns=["File Id", "Object Type", "Created At", "Assistant Id"]
    )
    for varFileId in varFileIds:
        file_data = f.retrieve_oai_assistant_files(varFileId=varFileId)
        df_oai_assistantfiles = df_oai_assistantfiles._append(file_data, ignore_index=True)
    return df_oai_assistantfiles

@st.cache_data
def create_dataframe_oai_assistanttools():
    varTools = st.session_state.assistant_tools
    df_oai_assistanttools = pd.DataFrame(
        columns=["Type"] 
    )
    for varTool in varTools:
        tool_data = f.retrieve_oai_assistant_tools(varTool=varTool)
        df_oai_assistanttools = df_oai_assistanttools._append(tool_data, ignore_index=True)
    return df_oai_assistanttools
        