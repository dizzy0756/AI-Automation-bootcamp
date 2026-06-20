#program : to be used as a module for the student file project
#function : search a particular student by name and return the info on the student if found, otherwise returns not found.


def search_student(students):
    found = False
    name = input("Enter the name of the student you want to search : ")
    for i, j in students.items():
        if i == name:
            print("-------------Student found--------------\n")
            print(f"Name : {i}      Marks Obtained : {j}")
            print("\n----------------------------------------")
            found == True
            return
    if found == False:
        print("Not found")    
    
# students = {
#     "John": 85,
#     "Alice": 92,
#     "Bob": 78
# }

# search_student(students)