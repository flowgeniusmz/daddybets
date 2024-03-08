import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def retrive_oia_files(varFileId):
    response = client.files.retrieve(
        file_id=varFileId
    )
    file_object = {
        "Id": response.id,
        "Object": response.object,
        "Bytes": response.bytes,
        "Created At": response.created_at,
        "Name": response.filename,
        "Purpose": response.purpose
    }
    return file_object

def retrieve_oai_assistant_files(varFileId):
    response = client.beta.assistants.files.retrieve(
        file_id=varFileId,
        assistant_id=st.session_state.assistant.id
        )
    file_object = {
        "File Id": response.id,
        "Object Type": response.object,
        "Created At": response.created_at,
        "Assistant Id": response.assistant_id
    }
    return file_object
    
def retrieve_oai_assistant_tools(varTool):
    tool_type = varTool.type
    tool_object = {
        "Type": tool_type
    }
    return tool_object
  
    
    
    
    