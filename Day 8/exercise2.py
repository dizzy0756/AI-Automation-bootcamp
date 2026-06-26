# Exercise 2
# Read the JSON file back and display its contents.

import json

with open("student.json","r") as file:
    content = json.load(file)

print(content)