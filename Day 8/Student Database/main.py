import json
from student import Student
from students_manager import StudentManager

try:
    with open("students.json","r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = []

students_list=[Student.from_dict(item) for item in data]
students = StudentManager(students_list)

while True:
    print("------------Menu-------------\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")
    print("\n-----------------------------")

    while True:
        try:
            choice = int(input("Choose an option : "))
            break
        except ValueError:
            print("Invalid Option")

    match choice:
        case 1:
            name = input("Enter the name of the Student : ")
            age = int(input("Enter the age of the Student : "))
            roll_no = int(input("Enter the roll no of the Student : "))

            student = Student(name,age,roll_no)
            students.add_student(student)
            
        case 2:
            students.view_students()

        case 3:
            name = input("Enter the name of the Student you want to search : ")
            students.search_student(name)

        case 4:
            students.save_students()
            break
     
        case _:
            print("Invalid Option")