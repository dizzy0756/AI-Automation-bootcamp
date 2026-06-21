# program : to be used as a module in main.py
# function : calculates total expenses.

def calculate_total_expenses(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if content == "":
                return "No expenses to calculate"
            
            amounts = []

            for line in content.splitlines(): # Tea     $30
                if line.strip():
                    parts = line.split()    #['Tea', '$30']
                    amount = int(parts[-1].replace("₹",""))
                    amounts.append(amount)

            return sum(amounts)
    except FileNotFoundError:
        print("File not found")