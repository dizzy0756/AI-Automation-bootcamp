# Exercise 3
# Store a list of books/products/employees in a JSON file and print each item neatly.

import json

items= {
    "books" : ["Abc","Asd","Qwerty"],
    "products" : ["Car","Watch","Guitar"],
    "employees" : ["Rahul","Gopi","Raj"]
}
with open("items.json","w") as file:
    json.dump(items, file, indent = 4)

print(json.dumps(items, indent=4))