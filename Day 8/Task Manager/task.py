class Task:
    def __init__(self,title,is_completed):
        self.title = title
        self.is_completed = is_completed
    
    def to_dict(self):
        return{
            "Title" : self.title,
            "Completed" : self.is_completed
        }
    
    def display(self):
        print(f"{self.title:<30}{self.is_completed}")
    
    @classmethod
    def from_dict(cls,data):
        return cls(title = data["Title"],is_completed = data["Completed"])