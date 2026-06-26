class Student:
    def __init__(self,name,roll_no,age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

    def to_dict(self):
        return {
            "name" : self.name,
            "roll_no" : self.roll_no,
            "age" : self.age
        }
    
    def display(self):
        print(f"{self.name:<20}{self.roll_no:<20}{self.age}")
    
    @classmethod
    def from_dict(cls,data):
        return cls(name = data["name"], roll_no = data["roll_no"], age = data["age"])
    
