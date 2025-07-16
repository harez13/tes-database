import sqlite3

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
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
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (name, email, umur, divisi))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data