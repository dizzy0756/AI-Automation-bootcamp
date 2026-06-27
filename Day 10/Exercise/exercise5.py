import sqlite3

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE author = 'Prasanta Naorem'")
