"""
This module serves as the command-line interface (CLI) for the Todo application.
"""

from .todo_app import TodoApp

def display_menu():
    """Displays the main menu to the user."""
    print("\n--- AI-Driven Todo App ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task Details")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Mark Task as Incomplete")
    print("7. Exit")
    print("--------------------------")

def handle_add_task(app: TodoApp):
    """Handles the logic for adding a new task."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    if title and description:
        task = app.add_task(title, description)
        print(f"Success: Task '{task.title}' added with ID {task.id}.")
    else:
        print("Error: Title and description cannot be empty.")

def handle_view_tasks(app: TodoApp):
    """Handles the logic for displaying all tasks."""
    tasks = app.get_all_tasks()
    if not tasks:
        print("No tasks to display.")
    else:
        print("\n--- All Tasks ---")
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {task.status}")
        print("-----------------")

def _get_task_id_from_user(prompt: str) -> int | None:
    """Gets a task ID from user input and handles potential errors."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Invalid ID. Please enter a number.")
        return None

def handle_update_task(app: TodoApp):
    """Handles the logic for updating a task's details."""
    task_id = _get_task_id_from_user("Enter the ID of the task to update: ")
    if task_id is None:
        return

    title = input("Enter the new title: ")
    description = input("Enter the new description: ")
    if not title or not description:
        print("Error: Title and description cannot be empty.")
        return

    task = app.update_task(task_id, title, description)
    if task:
        print(f"Success: Task {task_id} updated.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def handle_delete_task(app: TodoApp):
    """Handles the logic for deleting a task."""
    task_id = _get_task_id_from_user("Enter the ID of the task to delete: ")
    if task_id is None:
        return

    if app.delete_task(task_id):
        print(f"Success: Task {task_id} deleted.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def handle_update_task_status(app: TodoApp, status: str):
    """Handles the logic for updating a task's status."""
    task_id = _get_task_id_from_user(f"Enter the ID of the task to mark as {status}: ")
    if task_id is None:
        return

    task = app.update_task_status(task_id, status)
    if task:
        print(f"Success: Task {task_id} marked as {status}.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def main():
    """The main entry point for the CLI application."""
    app = TodoApp()

    actions = {
        '1': lambda: handle_add_task(app),
        '2': lambda: handle_view_tasks(app),
        '3': lambda: handle_update_task(app),
        '4': lambda: handle_delete_task(app),
        '5': lambda: handle_update_task_status(app, "complete"),
        '6': lambda: handle_update_task_status(app, "incomplete"),
    }

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '7':
            print("Exiting application. Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
