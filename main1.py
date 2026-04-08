import json  #gives us tools for working with JSON files. JSON is just a way to store data, like a notebook.
import os #This gives us tools for interacting with the computer/files. Used for checking "does this file exist"

FILE_NAME = "tasks.json" #name of the file where tasks will be stored

#Loads tasks from the JSON file if they exist
def load_tasks():
    if os.path.exists(FILE_NAME): #check if tasks.json exists 
        with open(FILE_NAME, "r") as file: #open the file in read mode 
            return json.load(file) #read JSON data and return it as a python list 

    return [] #If file doesnt exist, return a empty list


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    deadline = input("Enter your deadline, or leave blank: ").strip()
    priority = input("Enter the priority: ").strip().lower()

    task = {
        "title": title,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTo-Do List:")

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"

        print(
            f"{i}. {task['title']} | Deadline: {task['deadline']} | "
            f"Priority: {task['priority']} | Status: {status}"
        )


def remove_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input("Enter task number to remove: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)

            save_tasks(tasks)

            print(f"Removed '{removed['title']}'")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark complete: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True

            save_tasks(tasks)

            print(f"Marked '{tasks[index]['title']}' as completed.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List App ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            mark_completed(tasks)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

