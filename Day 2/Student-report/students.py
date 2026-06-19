def get_student_name():
    name = input("Enter the name of the student : ")
    return name

def get_student_roll_no():
    while True:
        try:
            roll_number = int(input("Enter the roll no. of the student : "))
            if(roll_number < 0):
                print("Roll no. of the student cannot be a negative number.")
            else:
                break
        except ValueError:
            print("Enter a valid integer value.")
    return roll_number

def get_student_marks():
    marks = {}
    subjects = ["Maths", "Science", "English"]

    for subject in subjects:
        while True:
            try:
                marks[subject] = int(input(f"Enter the marks scored in {subject} : "))
                break
            except ValueError:
                print("Enter a valid whole number")
    
    return marks