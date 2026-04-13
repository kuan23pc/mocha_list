import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def safe_input(prompt):
    """Read input safely without crashing on Ctrl+C or EOF."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return None


# Load tasks from file if it exists, otherwise return empty list
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Warning: tasks.json has an invalid format. Starting with an empty task list.")
                return []

            valid_tasks = []
            for task in data:
                if isinstance(task, dict) and "title" in task and "completed" in task:
                    if not isinstance(task["title"], str):
                        continue
                    if not isinstance(task["completed"], bool):
                        continue

                    if "deadline" not in task:
                        task["deadline"] = None

                    valid_tasks.append(task)

            if len(valid_tasks) != len(data):
                print("Warning: Some invalid tasks were ignored.")

            return valid_tasks

    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted or invalid. Starting with an empty task list.")
        return []
    except OSError as error:
        print(f"Error reading file: {error}")
        return []


tasks = load_tasks()


# Save tasks to json file
def save_tasks():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error saving file: {error}")


# Function to add a new task
def add_task():
    task = safe_input("Enter task: ")
    if task is None:
        return

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": task,
        "completed": False,
        "deadline": None
    })
    save_tasks()
    print(f"Task '{task}' added!")


# Display all tasks with their completion status
def show_tasks():
    if not tasks:
        print("👎 No tasks available. Add a new task!")
        return

    total = len(tasks)
    done = sum(task["completed"] for task in tasks)

    print(f"\n📝 Task List: ({total} tasks)")
    print(f"✅ Completed tasks: {done}/{total}\n")

    for i, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task["completed"] else "❌ Not Completed"
        deadline = task.get("deadline")
        deadline_text = f" (Deadline: {deadline})" if deadline else ""
        print(f"{i}. {task['title']}{deadline_text}: {status}")


# Function to delete a task
def delete_tasks():
    if not tasks:
        print("No tasks available to delete.")
        return

    show_tasks()

    task_to_delete = safe_input("Enter the task number to delete: ")
    if task_to_delete is None:
        return

    if task_to_delete == "":
        print("Task number cannot be empty.")
        return

    if not task_to_delete.isdigit():
        print("Please enter a valid number.")
        return

    index = int(task_to_delete) - 1

    if index < 0 or index >= len(tasks):
        print("Task number not found.")
        return

    removed_task = tasks.pop(index)
    save_tasks()
    print(f"Task '{removed_task['title']}' deleted!")


# Function to mark a task as completed
def mark_task_completed():
    if not tasks:
        print("No tasks available.")
        return

    show_tasks()

    task_to_complete = safe_input("Enter the task number to mark as completed: ")
    if task_to_complete is None:
        return

    if task_to_complete == "":
        print("Task number cannot be empty.")
        return

    if not task_to_complete.isdigit():
        print("Please enter a valid number.")
        return

    index = int(task_to_complete) - 1

    if index < 0 or index >= len(tasks):
        print("Task number not found.")
        return

    tasks[index]["completed"] = True
    save_tasks()
    print(f"Task '{tasks[index]['title']}' marked as completed!")


def sort_tasks(task_list):
    if not task_list:
        return []
    return sorted(task_list, key=lambda task: task["title"].lower())


# Function for deadline
def set_deadline():
    if not tasks:
        print("No tasks available.")
        return

    show_tasks()

    choice = safe_input("Enter task number to set deadline: ")
    if choice is None:
        return

    if choice == "":
        print("Task number cannot be empty.")
        return

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Task not found.")
        return

    deadline = safe_input("Enter deadline (YYYY-MM-DD): ")
    if deadline is None:
        return

    if deadline == "":
        print("Deadline cannot be empty.")
        return

    try:
        parsed_deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError:
        print("Please enter a valid date in YYYY-MM-DD format.")
        return

    today = datetime.today().date()

    if parsed_deadline < today:
        print("Deadline cannot be in the past.")
        return

    tasks[index]["deadline"] = deadline
    save_tasks()
    print(f"⏰ Deadline added to '{tasks[index]['title']}'!")


# Main program loop
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Delete tasks")
    print("4. Mark task as completed")
    print("5. Set deadline")
    print("6. Exit")

    choice = safe_input("Choose an option: ")
    if choice is None:
        continue

    if choice not in {"1", "2", "3", "4", "5", "6"}:
        print("Invalid choice. Please enter a number from 1 to 6.")
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
        set_deadline()
    elif choice == "6":
        print("Goodbye!")
        break