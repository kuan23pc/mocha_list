import json
import os

FILE_NAME = "tasks.json"

def safe_input(prompt):
    # read input safely without crashing on Ctrl+C or EOF.
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return None

def load_tasks():
    # load tasks safely from JSON file.
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Warning: tasks.json is not in the correct format. Starting with empty task list.")
                return []

            # This is to make sure all items are strings
            valid_tasks = [task for task in data if isinstance(task, str)]
            if len(valid_tasks) != len(data):
                print("Warning: some invalid tasks were ignored.")

            return valid_tasks

    except json.JSONDecodeError:
        print("Warning: invalid JSON. Starting with empty task list.")
        return []
    except OSError as error:
        print(f"Error reading file: {error}")
        return []

tasks = load_tasks()
completed = [False] * len(tasks)

def save_tasks():
    # save tasks safely.
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error saving tasks: {error}")

# Function to add a new task
def add_task():
    task = safe_input("Enter task: ")
    if task is None:
        return

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append(task)
    completed.append(False)
    save_tasks()
    print(f"Task '{task}' added!")

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for i in range(len(tasks)):
        status = "Completed" if completed[i] else "Not Completed"
        print(f"{i + 1}. {tasks[i]} [{status}]")

def delete_tasks():
    if not tasks:
        print("No tasks available to delete.")
        return

    task_to_delete = safe_input("Enter the task to delete: ")
    if task_to_delete is None:
        return

    if task_to_delete == "":
        print("Task name cannot be empty.")
        return

    if task_to_delete in tasks:
        index = tasks.index(task_to_delete)
        removed_task = tasks.pop(index)
        completed.pop(index)
        save_tasks()
        print(f"Task '{removed_task}' deleted!")
    else:
        print("Task not found.")

def mark_task_completed():
    if not tasks:
        print("No tasks available.")
        return

    task_to_complete = safe_input("Enter the task to mark as completed: ")
    if task_to_complete is None:
        return

    if task_to_complete == "":
        print("Task cannot be empty.")
        return

    if task_to_complete in tasks:
        index = tasks.index(task_to_complete)
        completed[index] = True
        save_tasks()
        print(f"Task '{tasks[index]}' marked as completed!")
    else:
        print("Task not found.")

def sort_tasks(task_list):
    if not task_list:
        return []
    return sorted(task_list)

def set_deadline(task, deadline):
    return task + " (deadline: " + deadline + ")"

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Delete tasks")
    print("4. Mark task as completed")
    print("5. Exit")

    choice = safe_input("Choose an option: ")
    if choice is None:
        continue

    if choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_tasks()
    elif choice == "4":
        mark_task_completed()
    elif choice == "5":
        print("Goodbye!")
        break