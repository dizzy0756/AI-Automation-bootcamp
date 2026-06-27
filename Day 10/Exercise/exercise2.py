import sqlite3

def get_books():
    books_len = int(input("Enter the number of books you want to add : "))
    books = []
    for i in range(books_len):
        title = input(f"Enter the title of Book {i+1} : ")
        author = input("Enter the name of the author : ")
        year = int(input("Enter the year it was published : "))
        book = (i+1,title, author, year)
        books.append(book)
    return books

books = get_books()

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()

    cursor.executemany(
        "INSERT INTO books(id , title, author, year) VALUES(?,?,?,?)",
        books
    )