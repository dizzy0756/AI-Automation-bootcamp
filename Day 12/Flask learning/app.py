from flask import Flask, request

app = Flask(__name__)

student_collection = []

@app.post("/students")
def add_student():

    data = request.get_json()
    
    student_collection.extend(data)

    return {
        "message" : "Student added successfully"
    }



@app.get("/students")
def view_students():
    return student_collection

@app.put("/students/<int:id>")
def update_student(id):
    data = request.get_json()
    for student in student_collection:
        if student["id"] == id:
            student.update(data)

    return {
        "message" : "student updated"
    }

@app.delete("/students/<int:id>")
def delete_student(id):
    for student in student_collection:
        if student["id"] == id:
            student_collection.remove(student)
            return {
                "message" : "Successfully deleted"
            }
        
    return {
        "message" : "Could not find the student"
    }

if __name__ == "__main__":
    app.run(debug=True)