class Contact:
    def __init__(self,id,name,number,email):
        self.id = id
        self.name = name
        self.number = number
        self.email = email

    # def update(self,field,value):
    #     if field == "name":
    #         self.name = value
    #     elif field == "number":
    #         self.number = value
    #     else:
    #         self.email = value

    def display(self):
        print(f"{self.id:<10}{self.name:<30}{self.number:<20}{self.email}")

    def to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "number" : self.number,
            "email" : self.email
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(id = data["id"], name = data["name"], number = data["number"], email = data["email"])
    