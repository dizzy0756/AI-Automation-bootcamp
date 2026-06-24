#Abstract class

from abc import ABC, abstractmethod

class Human(ABC):        
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def go_to_work(self):
        pass

class Teacher(Human):
    def work(self):
        print("teaches students")

    def go_to_work(self):
        print("Go to School")

class Doctor(Human):
    def work(self):
        print("treats Patients")

    def go_to_work(self):
        print("Go to Hospital")

teacher = Teacher()
doctor = Doctor()
teacher.go_to_work()
teacher.work()
doctor.go_to_work()
doctor.work()
