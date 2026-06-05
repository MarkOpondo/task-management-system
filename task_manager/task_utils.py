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
    print("Task marked as complete")

def view_pending_tasks(tasks=tasks):
    print("Pending tasks")

def calculate_progress(tasks = tasks):
    print("progress")
