import sqlite3
from model.contact import Contact

with sqlite3.connect("contacts.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   number TEXT NOT NULL,
                   email TEXT NOT NULL
                   )
    """)

def add(contact):
    with sqlite3.connect("contacts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contacts(id, name, number, email) VALUES (?, ?, ?, ?)",
                       (
                           contact.id,
                           contact.name,
                           contact.number,
                           contact.email
                       )
                    )
        
def update(contact):
    with sqlite3.connect("contacts.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE contacts
                        SET name = ?,
                       number = ?,
                       email = ?
                       WHERE id = ?
                       """,
                       (
                        contact.name,
                        contact.number,
                        contact.email,
                        contact.id
                       )
                    )
        
def delete(id):
    with sqlite3.connect("contacts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?",
                       (id,)
                       )

def search(id):
    with sqlite3.connect("contacts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = ?",
                       (id,)
                       )
        row = cursor.fetchone()
        if row is None:
            return None
        return Contact(row[0],row[1],row[2],row[3])

def display():
    with sqlite3.connect("contacts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        if rows is None:
            return None
        contacts = []
        for row in rows:
            contact = Contact(row[0],row[1],row[2],row[3])
            contacts.append(contact)
        return contacts
    

if __name__ == "__main__":
    print("Database testing")