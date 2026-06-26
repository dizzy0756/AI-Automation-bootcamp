# Exercise 5
# Modify an existing JSON file by adding a new record and saving the changes.

import json
with open("student.json", "r") as file:
    student = json.load(file)

new_record = ["address","wangjing"]
student[new_record[0]] = new_record[-1]

with open("student.json","w") as file:
    json.dump(student, file, indent=4)