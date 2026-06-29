import sqlite3

DB_NAME = "data.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    conn = get_connection

    conn.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


    
    