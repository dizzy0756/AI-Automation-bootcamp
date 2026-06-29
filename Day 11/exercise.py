import requests

class Post:
    def __init__(self,id,title,body):
        self.id = id
        self.title = title
        self.body = body

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "body" : self.body
        }
    
    def display(self):
        print(f"id : {self.id}")
        print(f"Title : {self.title}")
        print(f"Body : {self.body}")
        
    @classmethod
    def from_dict(cls,data):
        return cls(id = data["id"], title = data["title"], body = data["body"])
    
def create_post(post):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(
        url, json = post.to_dict()
    )

    if response.status_code == 201:
        created_post = Post.from_dict(response.json())
        return created_post  
    else:
        print(f"Could not create the request {response.status_code}")
        return None
    
post = Post(2,"Discipline","Discipline is the vital bridge between your ambitions and actual accomplishments. It isn't merely about rigid rules; it is the practice of self-control, consistency, and focus. By replacing impulsive actions with organized habits, discipline brings clarity to your life and empowers you to overcome challenges.")

new_post = create_post(post)
new_post.display()

