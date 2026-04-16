import tkinter as tk
from main import tasks, save_tasks #Hämtar tasks från main.py

def refresh_list():
    listbox.delete(0, tk.END) #Rensar listboxen
    for task in tasks:
        title = task["title"]
        status = "✅" if task["completed"] else "❌"
        deadline = task.get("deadline")
        deadline_text = f" (⏰ {deadline})" if deadline else ""
        listbox.insert(tk.END, f"{title} {status}{deadline_text}")

#Funktion när man klickar på "Add Task"
def add_task_gui():
    task = entry.get()
    if task:
        tasks.append({
            "title": task,
            "completed": False,
            "deadline": None
        })
        save_tasks()
        entry.delete(0, tk.END)
        refresh_list()

#Skapa fönstret
root = tk.Tk()
root.title("Task Manager")

#Inputfält
entry = tk.Entry(root)
entry.pack()

#Knapp
add_button = tk.Button(root, text="Add Task", command=add_task_gui)
add_button.pack()

#Lista
listbox = tk.Listbox(root, width=50)
listbox.pack()

#Ladda tasks vid start
refresh_list()

#Starta appen
root.mainloop()
