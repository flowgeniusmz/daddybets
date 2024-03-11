import streamlit as st
from openai import OpenAI
import pandas as pd
from datetime import datetime


client = OpenAI(api_key=st.secrets.openai.api_key)


a = client.files.create(
    file=open("data/dk_sportlist.csv", "rb"),
    purpose="assistants"
)
print(a)

