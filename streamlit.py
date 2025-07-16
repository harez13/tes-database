import streamlit as st

st.title('Test Database')

conn = st.connection('mysql', type='sql')

df = conn.query('select * from orders')

st.dataframe(df)