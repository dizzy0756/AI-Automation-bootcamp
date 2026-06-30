import requests
from model.contact import Contact


url="http://127.0.0.1:5000/contacts"

contact = {
    "id" : 2,
    "name" : "Buu Sorokhaibam",
    "number" : "+919846286762",
    "email" : "buuSorokhaibam@email.com"
}
# response = requests.post(url,
#             json=contact)
# print(response.text)

# response = requests.get(url)
# results = response.json()
# for result in results:
#     print(result)
url2 = "http://127.0.0.1:5000/contacts/2"
response = requests.put(url2,
                    json=contact)
print(response.text)

response = requests.get(url2)
print(response.json())