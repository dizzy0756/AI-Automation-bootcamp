class Post:
    def __init__(self,user_id,title,body):
        self.user_id = user_id
        self.title = title
        self.body = body

    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "title" : self.title,
            "body" : self.body
        }
    
    def display(self):
        print(f"User_id : {self.user_id}")
        print(f"Title : {self.title}")
        print(f"Body : {self.body}")
        
    @classmethod
    def from_dict(cls,data):
        return cls(user_id = data["userId"], title = data["title"], body = data["body"])