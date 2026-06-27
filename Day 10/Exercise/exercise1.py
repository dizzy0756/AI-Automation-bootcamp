import sqlite3

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   year INTEGER NOT NULL
    )
    """)