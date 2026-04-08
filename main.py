# List to store all tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter task: ") 
    tasks.append(task)
    print("Task added!")

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
# isabellas 
def sort_tasks(tasks):
    if not tasks:
        return[]
    return sorted(tasks)
#isabellas 6
def set_deadline(task,deadline):
    return task + "(deadline: " + deadline + ")"

#isabellas
def set_priority(task,priority):
    return task + "(priority: " + priority + ")"
