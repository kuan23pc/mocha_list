import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

tasks = load_tasks()
completed = [False] * len(tasks)

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task():
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return
     
    tasks.append(task)
    completed.append(False)
    save_tasks()
    print(f"Task '{task}' added!")


#Fun. to display all tasks
def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nTasks:")

    for i in range (len(tasks)):
        if completed[i]:
            print(f"- {tasks[i]} [Completed]")
        else:
            print(f"- {tasks[i]} [Not Completed]")

#Funktion to DELETE a task CO
def delete_tasks():
    if not tasks:
        print("No tasks available to delete.")
        return 
    
    task_to_delete = input ("Enter the task to delete: ").strip()

    if task_to_delete == "":
        print("Task name cannot be empty.")
        return
    
    if task_to_delete in tasks:
        index = tasks.index(task_to_delete)          #fins where task is 
        remove_task = tasks.pop(index)                #remove task 
        completed.pop(index)
        save_tasks()                           #remove matching status
        print(f"Task '{remove_task}' deleted!")
    else:
        print("Task not found.")

#FUnction to MARK a task as COMPLETED CO
def mark_task_completed():
    if not tasks:
        print("No tasks available.")
        return 
    
    task_to_complete = input ("Enter the task to mark as completed: ").strip()
   
    if task_to_complete == "":
        print("Task name cannot be empty.")
        return

    if task_to_complete in tasks:
        index= tasks.index(task_to_complete)  #Find task Position
        completed[index] = True
        save_tasks()               #mark as completed
        print(f"Task '{tasks[index]}' marked as completed!")
    else:
        print("Task not found.")
# function 
def sort_tasks(tasks):
    if not tasks:
        return[]
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
