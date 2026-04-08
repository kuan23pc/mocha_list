# List to store all tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return
     
    tasks.append(task)
    print(f"Task '{task}' added!")

# Fun. to display all tasks
def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nTasks:")

    for t in tasks:
        print(f"- {t}")

# Main program loop
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose an option: ") #User selects option

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break  #Exit program
    else:
        print("Invalid choice. Please try again.")
