import sqlite3

connection = sqlite3.connect("contacts.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               phone TEXT NOT NULL)
""")

contacts = [
    ("Pritam Laishram","+915235823744"),
    ("Jonita Sorokhaibam","+915278523744"),
    ("Lucky Pichimayum","+915235819284")
    ]
cursor.executemany(
    "INSERT INTO contacts(name , phone) VALUES (?, ?)",
    contacts
)

cursor.execute("DELETE FROM contacts WHERE id > 3")

cursor.execute("SELECT * FROM contacts")

rows = cursor.fetchall()

print(f"{'Name':<30}{'Phone No'}")
for row in rows:
    print(f"{row[1]:<30}{row[-1]}")

connection.commit()
connection.close()