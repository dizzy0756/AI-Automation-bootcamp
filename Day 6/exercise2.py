# Exercise 2

# Create a

# Person

# class.

# Create

# Student
# Teacher
# Developer

# that inherit from it.

# Each should override

# introduce()

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def introduce(self):
        print(f"Hello! My name is {self.name}")        

class Student(Person):
    def __init__(self, name, school_name):
        super().__init__(name)
        self.school_name = school_name
    def introduce(self):
        super().introduce()
        print(f"I study in {self.school_name}")

class Teacher(Person):
    def __init__(self, name, subject_name):
        super().__init__(name)
        self.subject_name = subject_name
    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject_name}")


class Developer(Person):
    def __init__(self, name, developer_type):
        super().__init__(name)
        self.developer_type = developer_type
    def introduce(self):
        super().introduce()
        print(f"I am {'an' if self.developer_type[0] == 'a' or 'e' or 'i' or 'o' or 'u' else 'a'} {self.developer_type} developer")

people = [Student("Rahul","ABC Institute"), Teacher("Raj","Mathematics"), Developer("Jai","frontend")]

for person in people:
    person.introduce()