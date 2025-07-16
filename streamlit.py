import streamlit as st
from database import init_db, insert_data, fetch_all

st.set_page_config(page_title="Data Input App", layout="centered")

# Inisialisasi DB
init_db()

st.title("📋 INPUT KINERJA ITSUPPORT")

with st.form("data_form"):
    name = st.text_input("Nama Lengkap")
    email = st.text_input("Email")
    umur = st.number_input("Umur", min_value=1, max_value=120)
    divisi = st.text_input("Divisi")
    submitted = st.form_submit_button("Kirim")

    if submitted:
        if name and email:
            insert_data(name, email, umur, divisi)
            st.success("✅ Data berhasil disimpan!")
        else:
            st.warning("⚠️ Mohon lengkapi semua kolom!")

st.write("## 📑 Data Tersimpan")
data = fetch_all()
if data:
    st.dataframe(data)
else:
    st.info("Belum ada data.")