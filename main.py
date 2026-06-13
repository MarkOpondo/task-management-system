# from validation import validate_task_title, validate_task_description, validate_due_date
# from task_utils import add_task, tasks, mark_task_as_complete, view_pending_tasks
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
    id = int(index) - 1
    if 0 <= id < len(tasks):
        tasks[id]["completed"] = True
        print("Task marked as complete!")

    else:
        print("Task does not exist")

def view_pending_tasks(tasks=tasks):
    pending = (for t in tasks if not t["completed"])
    if pending:
        for task in pending:
            print("Pending.... ")
            print("-"*30)
            print(task)
    else:
        print("No pending tasks")

def calculate_progress(tasks = tasks):
    if len(tasks) > 0:
        completed_tasks = sum(1 for t in tasks if t["completed"])
        all_tasks = len(tasks)
        progress = (completed_tasks / all_tasks) * 100
        print(progress)
    else: 
        print("No tasks available")


def validate_task_title(title):
    if not title:
        raise ValueError("Title cannot be empty")
    

def validate_task_description(description):
    if not description:
        raise ValueError("Description cannot be empty")

def validate_due_date(due_date):
    if not due_date:
        raise ValueError("Due date cannot be empty")
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except:
        raise ValueError("Invalid date format YYYY-MM-DD")


def main():
    while True:
        # print(tasks)
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter your task title: ")
            description = input("Task Description: ")
            due_date = input("Task Due Date YYYY-MM-DD: ")

            try:
                validate_task_title(title)
                validate_task_description(description)
                validate_due_date(due_date)

                add_task(title, description, due_date)

                print("Task added successfully!", tasks)
            except ValueError as e:
                print("Input Error", str(e))

        elif choice == "2":
            index = input("Enter the task number: ")
            try: 
                mark_task_as_complete(index, tasks)
            except ValueError as e:
                print("Task does not exist", str(e))

        elif choice == "3":
            try:
                view_pending_tasks(tasks)
            except ValueError as e:
                print("No pending tasks")
            
        elif choice == "4":
                calculate_progress(tasks)
            

        elif choice == "5":
            print("Exiting the programme")
            break


if __name__ == "__main__":
    main()