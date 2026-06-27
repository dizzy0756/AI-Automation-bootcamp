import sqlite3

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books WHERE year > 2020")

    books = cursor.fetchall()

print(f"{'Title':<20}{'Author':<20}{'Year'}")
for book in books:
    print(f"{book[1]:<20}{book[2]:<20}{book[-1]}")