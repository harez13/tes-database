import sqlite3
import pandas as pd

DB_NAME2 = "data2.db"

def init_db2():
    conn = sqlite3.connect(DB_NAME2)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pegawai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            umur INTEGER,
            divisi TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_data2(name, email, umur, divisi):
    conn = sqlite3.connect(DB_NAME2)
    c = conn.cursor()
    c.execute("INSERT INTO pegawai(name, email, umur, divisi) VALUES (?, ?, ?, ?)", (name, email, umur, divisi))
    conn.commit()
    conn.close()

def fetch_all2():
    with sqlite3.connect(DB_NAME2) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM pegawai ORDER BY id DESC")
        data = c.fetchall()
        
        column = [col[0] for col in c.description]

    return pd.DataFrame(data, columns=column)
    conn.close()