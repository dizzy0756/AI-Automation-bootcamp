def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    print("==== Calculator ====\n")
    print("1. Add")
    print("2 Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")
    choice = int(input("Choice: "))
    if(choice == 5):
        break
    print()
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print()
    match choice:
        case 1:
            print(f"Answer = {add(num1,num2)}")
        case 2:
            print(f"Answer = {subtract(num1,num2)}")
        case 3:
            print(f"Answer = {multiply(num1,num2)}")
        case 4:
            if num2 == 0:
                print("Division by 0 is undefined)")
            else:
                print(f"Answer = {divide(num1,num2)}")
        case 5:
            break
        case _:
            print("Invalid choice")
    print()
    continue_choice = input("Do another calculation? (Y/N)")
    if (continue_choice == "N" or continue_choice =="n"):
        break