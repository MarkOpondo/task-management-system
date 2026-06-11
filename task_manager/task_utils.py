from datetime import datetime
# Validation functions import

tasks = []

def add_task(title, description, due_date):
    task = {
        "title" : title,
        "description" : description,
        "due_date" : due_date,
        "completed" : False
    }
    tasks.append(task)


def mark_task_as_complete(index, tasks=tasks):
    for task in tasks:
        if index == task["title"]:
            task["completed"] = True
            print("Task marked as complete!")

        else:
            print("Task does not exist")

def view_pending_tasks(tasks=tasks):
    for task in tasks:
        if task["completed"] == False:
            print("Pending.... ")
            print("-"*30)
            print(task)
        else:
            print("No pending tasks")

def calculate_progress(tasks = tasks):
    print("progress")
