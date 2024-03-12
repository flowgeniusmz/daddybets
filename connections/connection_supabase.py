import streamlit as st
from st_supabase_connection import SupabaseConnection
from supabase import Client, create_client

@st.cache_resource
def supabase_connection_initialize():
    url = st.secrets.supabase.url
    key = st.secrets.supabase.api_key
    key_admin = st.secrets.supabase.api_key_admin

    Client = create_client(supabase_key=key_admin, supabase_url=url)
    return Client