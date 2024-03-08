import streamlit as st

def read_get_file(varPath):
    
    with open(varPath, "r") as file:
        file_path_content = file.read()
        return file_path_content