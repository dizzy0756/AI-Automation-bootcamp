import json
import utils
from task import Task
from task_manager import Tasks

try:  
    with open("Task_manager.json","r") as file:
        data = json.load(file)

except FileNotFoundError:
        data = []

contents = [Task.from_dict(item) for item in data]
tasks = Tasks(contents)

while True:
    print("------------Menu-------------\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Complete")
    print("5. Exit")
    print("\n-----------------------------")

    while True:
        try:
            choice = int(input("Choose an option : "))
            break
        except ValueError:
            print("Invalid Option")

    match choice:
        case 1:
            title = input("Enter the name of the task : ")
            tasks.add_task(title)
        case 2:
            tasks.view_tasks()
        case 3:
            title = input("Enter the name of the task you want to remove : ")
            tasks.remove_task(title)
        case 4:
            title = input("Enter the name of the task :")
            tasks.complete_task(title)
        case 5:
            tasks.save_tasks()
            break
        case _:
            print("Invalid Option")