import requests

url = "http://127.0.0.1:5000/about"
response = requests.get(url)
result = response.json()

if result:
    print(f"Name : {result["name"]}")
    print(f"Course : {result["course"]}")
    print(f"Age : {result["age"]}")