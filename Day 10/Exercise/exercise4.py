import sqlite3

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE books SET year = ? WHERE author = ?",
        (2017,"Prasanta Naorem")
    )