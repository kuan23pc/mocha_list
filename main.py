import json
import os

FILE_NAME = "tasks.json"
#load task from file if it exists,otherwise return empty list
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

tasks = load_tasks()

#save tasks to json file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

#Function to add a new task
def add_task():
    task = input("Enter task: ").strip()

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

    task_to_delete = input ("Enter the task number to delete: ").strip() #frågan efter task nummer

    if task_to_delete == "":
        print("Task number cannot be empty.")
        return

    if not task_to_delete.isdigit():  #kontrollera att det är en siffra 
        print("Please enter a valid number.")
        return 
    
    index = int(task_to_delete) - 1 #omvandla till pyhton index (python börjar på 0, användare börjar på 1)

    if index < 0 or index >= len(tasks):
        print("Task number not found.")
        return 
    
    removed_task= tasks.pop(index)
    print(f"Task '{removed_task['title']}' deleted!")

#FUnction to MARK a task as COMPLETED CO
def mark_task_completed():
    if not tasks:
        print("No tasks available.")
        return 
    
    task_to_complete = input ("Enter the task to mark as completed: ").strip()

    if task_to_complete == "":
        print("Task name cannot be empty.")
        return
    for task in tasks:
        if task["title"] == task_to_complete:
            task["completed"] = True
            save_tasks()
            print(f"Task '{task['title']}' marked as completed!")
            return
    

    print("Task not found.")
   
    # optional: add deadline to a task(not integrated)
def sort_tasks(tasks):
    if not tasks:
        return []
    return sorted(tasks)

# function for deadline
def set_deadline():
    if not tasks:
        print("No tasks available.")
        return
    
    show_tasks()
    choice = input("Enter task number to set deadline: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Task not found.")
        return
    
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()

    if deadline == "":
        print("Deadline cannot be empty.")
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

    choice = input("Choose an option: ") #User selects option

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
        break  #Exit program
    else:
        print("Invalid choice. Please try again.")
