#program : to be used as a module for the student file project
# adds students into a dict variable

def add_student_info():

    students = {}
    while True:
        name = input("Enter the name of the student or enter 'done' to stop : ")
        if name == "done":
            break
        while True:
            try:
                mark = int(input("Enter marks obtained by the students : "))
                break
            except ValueError:
                print("Enter a valid whole number.")
        students[name] = mark

    return students

check = add_student_info()

for i, value in check.items():
    print(i, value)