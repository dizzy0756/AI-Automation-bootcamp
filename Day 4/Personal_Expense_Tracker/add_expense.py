# program : to be used as a module in main.py
# function : adds a new expense.

def add_exp():
    expense = {}

    while True:

        title = input("Enter the title of the expense or 'done' if completed : ")
        if title == "done":
            break

        while True:
            try:
                amount = int(input(f"Enter the amount expent on {title} : "))
                break
            except ValueError:
                print("Enter a valid positive integer")

        expense[title] = amount

    return expense

def add_to_file(expense,file_name):

    content = ""
    for title, amount in expense.items():
        content += f"{title:<10}₹{amount}\n"

    try:
        with open(file_name, "w") as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found")