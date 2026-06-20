#program : to be used as a module for the student file project
#function : displays all the students information.


def view_students(students):
    print("------------------------------------------------\n")
    for name, mark in students.items():
        print(f"Name : {name}\tMarks Obtained: {mark}")
    print("\n------------------------------------------------")

students = {
    "John": 85,
    "Alice": 92,
    "Bob": 78
}

view_students(students)