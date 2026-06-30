from flask import request
from database import database
from model.contact import Contact

def generate_routes(app):

    @app.post("/contacts")
    def add_contact():
        data = request.get_json()
        contact = Contact.from_dict(data)
        database.add(contact)
        return{
            "message" : "Contact added Successfully"
        }, 201
    
    @app.put("/contacts/<int:id>")
    def update_contact(id):
        data = request.get_json()
        data["id"] = id
        contact = Contact.from_dict(data)
        database.update(contact)
        return{
            "message" : "Contact updated Successfully"
        }, 200
    
    @app.delete("/contacts/<int:id>")
    def delete_contact(id):
        database.delete(id)
        return{
            "message" : "Contact deleted Successfully"
        }, 200
    
    @app.get("/contacts/<int:id>")
    def search_contact(id):
        result = database.search(id)
        if result is None:
            return {
                "message" : "No contact found"
            }, 404
        return result.to_dict(), 200
    
    @app.get("/contacts")
    def view_contacts():
        contacts = database.display()
        result = []
        for contact in contacts:
            result.append(contact.to_dict())
        return result, 200
    