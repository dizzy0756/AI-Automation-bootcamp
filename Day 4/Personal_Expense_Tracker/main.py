# program - Personal expense Tracker
# uses : tracks expenses with accuracy and efficiency
# future improvements: predicts how much amount can be saved at the end of the month after taking in the data about our expenses and income. 


import view
import total
import add_expense

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")
    while True:
        try:
            choice = int(input("Choose an option : "))
            break
        except ValueError:
            print("Enter a valid numeric option from the given menu")

    if choice == 4:
        break

    match choice:
        case 1:
            content = add_expense.add_exp()
            add_expense.add_to_file(content, "expenses.txt")
        case 2:
            view.view_expenses("expenses.txt")
        case 3:
            result = total.calculate_total_expenses("expenses.txt")
        case _:
            print("Invalid option")
