# Persist completed status feature
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

# Function to add a new task
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

    for task in tasks:
        status = "Completed" if task ["completed"] else "Not Completed"
        print(f"- {task['title']} [{status}]")
#delete a task by its title
def delete_tasks():
    if not tasks:
        print("No tasks available to delete.")
        return 
    
    task_to_delete = input ("Enter the task to delete: ").strip()

    if task_to_delete == "":
        print("Task name cannot be empty.")
        return
    
    for i, task in enumerate(tasks):
        if task ["title"] == task_to_delete:
            removed_task = tasks.pop(i)
            save_tasks()
            print(f"Task '{removed_task['title']} deleted!")
            return
        
    
    print("Task not found.")
#mark a task as completed
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
