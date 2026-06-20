#program : to be used as a module for the student file project
#function: returns the average mark obtained by the students.

def find_average(students):
    average = sum(students.values()) / len(students)
    return average

# students = {
#     "John": 85,
#     "Alice": 92,
#     "Bob": 78
# }

# print(find_average(students))