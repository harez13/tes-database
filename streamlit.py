import streamlit as st
import mysql.connector

st.title('Test Database')

conn = mysql.connector.connect(
    host = st.secrets['mysql']['host'],
    port = st.secrets['mysql']['port'],
    database = st.secrets['mysql']['database'],
    user = st.secrets['mysql']['user'],
    password = st.secrets['mysql']['password']
)