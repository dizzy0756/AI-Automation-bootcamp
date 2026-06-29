import requests
from model import Post

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
    
def view_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    results = response.json()
    if response.status_code == 200:
        if results:
            for result in results:
                post_obj = Post.from_dict(result)
                post_obj.display()
                print()
        else:
            print("No Posts available")
    else:
        print(f"Failed to retrieve data {response.status_code}")

def search_post(user_id):
    found = False
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    results = response.json()
    if response.status_code == 200:
        if results:
            for result in results:
                if user_id == result["user_id"]:
                    post_obj = Post.from_dict(result)
                    post_obj.display()
                    found = True
                    break
            if found is False:
                print(f"No post with User_Id {user_id} exist")
        print("No Posts available")
    else:
        print(f"Failed to retrieve data {response.status_code}")

def view_users():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    results = response.json()
    if response.status_code == 200:
        if results:
            for result in results:
                post_obj = Post.from_dict(result)
                print(post_obj.user_id)
        else:
            print("No Posts available")
    else:
        print(f"Failed to retrieve data {response.status_code}")

view_post()