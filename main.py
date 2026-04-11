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
    tasks.append({"title": task, "completed": False})
    save_tasks()
    print(f"Task '{task}' added!")

#display all tasks with their completion status
def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nTasks:")

    for i in range (len(tasks)):
        if completed[i]:
            print(f"{i+1}. {tasks[i]} [Completed]")
        else:
            print(f"{i+1}. {tasks[i]} [Not Completed]")

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
    completed.pop(index)
    print(f"Task '{removed_task}' deleted!")

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
def set_deadline(task,deadline):
    return task + "(deadline: " + deadline + ")"


# Main program loop
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Delete tasks")
    print("4. Mark task as completed")
    print("5. Exit")

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
        break  #Exit program
    else:
        print("Invalid choice. Please try again.")
