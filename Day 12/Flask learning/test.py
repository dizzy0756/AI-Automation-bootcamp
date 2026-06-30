import requests

url_1 = "http://127.0.0.1:5000/students"

student = [
    {
        "id" : 1,
        "name" : "Pritam Laishram",
        "course" : "AI Automation",
        "age" : 20
    },
    {
        "id" : 2,
        "name" : "Jonita Sorokhaibam",
        "course" : "Manipuri Literature",
        "age" : 18
    },   
    {
        "id" : 3,
        "name" : "Lucky Pichimayum",
        "course" : "Business",
        "age" : 21
    }   
]    

response = requests.post(url_1,json=student)
print(response.json())

response = requests.get(url_1)
results = response.json()
for result in results:
    print(result)

id_no = 3
url = f"http://127.0.0.1:5000/students/{id_no}"
response = requests.delete(url)
print(response.json())

response = requests.get(url_1)
results = response.json()
for result in results:
    print(result)
