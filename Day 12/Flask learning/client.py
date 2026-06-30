import requests

id_number = 1
url = f"http://127.0.0.1:5000/students/{id_number}"
student = {
        "id" : 2,
        "name" : "Jonita Sorokhaibam",
        "course" : "Manipuri Literature",
        "age" : 19
    }
response = requests.put(
    url,
    json=student
    )

print(response.json())