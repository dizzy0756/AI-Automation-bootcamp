# Project : Employee_salary_calculator.
# Business problem: Manual calculation of wages leading to potential errors and time consumption
# Solutions: Quick and Accurate calculation of employee's wages
# Future improvements: Record calculation history along with date and time. Able to tell how much salary a particular employee recieved for a particular month.


employee_name = input("Enter employee name: ")
while True:
    try:
        hours_worked = int(input("Enter the hours worked by the employee: "))
        hourly_wage = int(input("Enter the hourly wage of the employee: "))
        break
    except ValueError:
        print("Enter a valid integer value.")

def calculate_wage(hour,rate):
    return hour*rate

print("\n----------- PAYSLIP -----------\n")
print(f"Employee : {employee_name}\n")
print(f"Hours Worked : {hours_worked}\n")
print(f"Hourly Wage : ₹{hourly_wage}\n")
if hours_worked > 160:
    extra_hours = hours_worked - 160
    bonus_wage = extra_hours * hourly_wage * 1.5
    print(f"Monthly Salary : {calculate_wage(hours_worked,hourly_wage) + bonus_wage}\n")
else:
    print(f"Monthly Salary : {calculate_wage(hours_worked,hourly_wage)}\n")
print("-------------------------------")