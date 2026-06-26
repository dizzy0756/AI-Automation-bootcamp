import json
from student import Student

class StudentManager:
    def __init__(self,students=None):
        if students  is None:
            self.students = []
        else:
            self.students = students

    def add_student(self,student):
        self.students.append(student)

    def search_student(self,name):
        found = False
        for student in self.students:
            if name == student.name():
                print("-----------------Student found-------------------\n")
                student.display()
                found = True
        if found == False:
            print("Student not found")
    
    def view_students(self):
        print(f"{'Name':<20}{'Roll no':<20}{'Age'}")
        for student in self.students:
            student.display()

    def save_students(self):
        students_list = []
        for student_obj in self.students:
            student_dict = student_obj.to_dict()
            students_list.append(student_dict)

        with open("students.json","w") as file:
            json.dump(students_list, file, indent=4)