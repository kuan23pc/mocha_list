import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
        return []

tasks = load_tasks()

with open(FILE_NAME, "w") as file:
    json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task():
    task = input("Enter task: ") 
    tasks.append(task)
    save_tasks()
    print("Task added!")

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indet=4)

# Fun. to display all tasks
def show_tasks():
    print("All tasks:")
    for t in tasks:
        print(t)

# Main program loop
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose: ") #User selects option

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break  #Exit program
