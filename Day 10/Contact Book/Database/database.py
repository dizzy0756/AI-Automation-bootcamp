import sqlite3

def create_contacts():
    with sqlite3.connect("contactBook.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       phone TEXT NOT NULL,
                       email TEXT NOT NULL 
            )                       
        """)

def add_contact(contact_id, name, number, email):
    with sqlite3.connect("contactBook.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contacts(id, name, phone, email) VALUES(?, ?, ?, ?)", 
            (contact_id, name, number, email)
            )

def update_contact(id,field,value):
    with sqlite3.connect("contactBook.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE contacts SET {field} = ? WHERE id = ?",
                                (value,id,)
                                )

def search_contact(name):
    with sqlite3.connect("contactBook.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name = ?",
                       (name,)
                       )
        result = cursor.fetchone()
        if result is None:
            print(f"No contact with the name '{name}' exist")
        else:
            print("-----------Found----------\n")
            print(f"Name : {result[1]:<20}Number : {result[2]:<20}Email : {result[-1]}")

def view_contacts():
    with sqlite3.connect("contactBook.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()

        if not rows:
            print("No contact found")
            return
        
        print(f"{'Id':<10}{'Name':<20}{'Number':<20}{'Email'}")
        for row in rows:
            print(f"{row[0]:<10}{row[1]:<20}{row[2]:<20}{row[-1]}")

def delete_contact(contact_id):
    with sqlite3.connect("contactBook.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?",
                       (contact_id,)
                       )
