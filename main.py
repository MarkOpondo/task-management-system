from validation import validate_task_title, validate_task_description, validate_due_date
from task_utils import add_task, tasks, mark_task_as_complete, view_pending_tasks

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
            title = input("Enter the title of completed task: ")
            try: 
                mark_task_as_complete(title, tasks)
            except ValueError as e:
                print("Task does not exist", str(e))

        elif choice == "3":
            try:
                view_pending_tasks(tasks)
            except ValueError as e:
                print("No pending tasks")

        elif choice == "5":
            print("Exiting the programme")
            break


if __name__ == "__main__":
    main()