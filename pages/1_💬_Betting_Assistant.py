import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from status.chatstatus import Status

# 0. Set Master Page Config (see config/pagesetup.py)
ps.master_page_config(1)

# 1. Check and/or Initialize Session States (see config/sessionstates.py)
ss.master_session_state()