# Exercise 4
# Convert a Python dictionary to a JSON string and back again using dumps() and loads()

import json
book = {
    "title" : "ABC",
    "author" : "XYZ"
}

json_string = json.dumps(book,indent=4)

print(json_string)

new_book = json.loads(json_string)
print(new_book)