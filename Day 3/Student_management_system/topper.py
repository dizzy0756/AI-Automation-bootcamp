#program : to be used as a module for the student file project
#function : returns the name of the student with the highest mark obtained.

def find_topper(students):
    topper = ""
    max_mark = max(students.values())
    for name, mark in students.items():
        if mark == max_mark:
            topper = name
            return topper
        
    return "Not found"

# students = {
#     "John": 85,
#     "Alice": 92,
#     "Bob": 78
# }

# print(find_topper(students))