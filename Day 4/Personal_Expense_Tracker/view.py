# program : to be used as a module in main.py
# function : views all the expenses.

def view_expenses(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
