# Exercise 1
# Create a Python dictionary representing a student and save it to a JSON file.

import json
student ={
    "name" : "Pritam",
    "age" : 20,
    "roll" : 20
}

with open("student.json","w") as file:
    json.dump(student, file, indent=4)

