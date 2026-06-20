# Project : Students Exam File
# problems solved : Accurate and efficient retrieval and updation of student information
# future improvement : Connect to a database and store the information
#                      Predict the average, topper or mark obtained by a student in future.

import add
import search
import topper
import average
import view


students={}

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Average Marks")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 6:
        break

    match choice:
        case 1:
            students = add.add_student_info(students)
        case 2:
            view.view_students(students)
        case 3:
            search.search_student(students)
        case 4:
            print(f"Topper : {topper.find_topper(students)}")
        case 5:
            print(f"Average marks obtained by the students : {average.find_average(students)}")
        case _:
            print("Invalid choice")