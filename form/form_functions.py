import streamlit as st
from connections import connection_supabase as connSB


supabase_client = connSB.supabase_connection_initialize()

def get_auth_data_json(varUsername, varCredential):
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    auth_data = {
        column_username: varUsername,
        column_credential: varCredential
    }
    return auth_data


def get_auth_select_string():
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    select_string = f"{column_username}, {column_credential}"
    return select_string

def add_new_user(varUsername, varCredential):
    table_users = st.secrets.loginform.user_tablename
    data_new_user = get_auth_data_json(varUsername=varUsername, varCredential=varCredential)
    data, _ = (supabase_client.table(table_name=table_users).insert(json=data_new_user).execute())
    return data, _

def check_existing_user(varUsername, varCredential):
    table_users = st.secrets.loginform.user_tablename
    select_string = get_auth_select_string()
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    data, _ = (supabase_client.table(table_name=table_users).select(select_string).eq(column=column_username, value=varUsername).eq(column=column_credential, value=varCredential).execute())
    length_data = len(data[-1])
    return length_data

def formfield_validation_auth(varUsername, varCredential, varButton):
    if varButton and varUsername is not None and varCredential is not None:
        return True
    else:
        return False
    
a = formfield_validation_auth("A", "B", "True")
print(a)