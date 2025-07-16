import sqlite3

DB_NAME = "datapegawai.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
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

def insert_data(name, email, umur, divisi):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO pegawai(name, email, umur, divisi) VALUES (?, ?, ?, ?)", (name, email, umur, divisi))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM pegawai ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data