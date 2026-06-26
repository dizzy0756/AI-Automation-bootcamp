from task import Task
import json

class Tasks:
    def __init__(self, tasks=None):
        if tasks is None:
            self.tasks = []
        else:
            self.tasks = tasks

    def add_task(self,title):
        task = Task(title)
        self.tasks.append(task)

    def remove_task(self,title):
        found = False
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove()
                found = True
        if found == False:
            print("Task does not exist")

    def complete_task(self,title):
        found = False
        for task in self.tasks:
            if task.title == title:
                self.is_complete = True
                found = True
        if found == False:
            print("Task does not exist")

    def view_tasks(self):
        print(f"{'Task':<30}{'Completed'}")
        for task in self.tasks:
            task.display()

    def save_tasks(self):
        tasks = []
        for task in self.tasks:
            task_in_dict = task.to_dict()
            tasks.append(task_in_dict)
        with open("Tasks_manager.json","w") as file:
            json.dump(tasks, file, indent=4)