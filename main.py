import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def safe_input(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return None

#load task from file if it exists,otherwise return empty list
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                print("Invalid task file format. Starting with an empty list.")
                return []
        except json.JSONDecodeError:
            print("Invalid JSON file. Starting with an empty list.")
            return []
        except OSError as error:
            print(f"Error reading file: {error}")
            return []
    return []

tasks = load_tasks()

#save tasks to json file
def save_tasks():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error saving file: {error}")

#Function to add a new task
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
        "deadline" : None
    })
    save_tasks()
    print(f"Task '{task}' added!")

#display all tasks with their completion status
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

#Funktion to DELETE a task CO
def delete_tasks():
    if not tasks:
        print("No tasks available to delete.") #kontrollera om listan är tom
        return 

    show_tasks() #visa alla tasks först 

    task_to_delete = safe_input("Enter the task number to delete: ")
    if task_to_delete is None:
        return

    if task_to_delete == "":
        print("Task number cannot be empty.")
        return

    if not task_to_delete.isdigit():  #kontrollera att det är en siffra 
        print("Please enter a valid number.")
        return 
    
    index = int(task_to_delete) - 1 #omvandla till python index (python börjar på 0, användare börjar på 1)

    if index < 0 or index >= len(tasks):
        print("Task number not found.")
        return 
    
    removed_task= tasks.pop(index)
    save_tasks()
    print(f"Task '{removed_task['title']}' deleted!")

#Function to MARK a task as COMPLETED CO
def mark_task_completed():
    if not tasks:
        print("No tasks available.")
        return 
    
    show_tasks() #visa alla tasks först

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

#optional: add deadline to a task(not integrated)
def sort_tasks(tasks):
    if not tasks:
        return []
    return sorted(tasks)

#function for deadline
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

#Main program loop
def main ():
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
            print("Invalid choice. Please try again.")
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
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()