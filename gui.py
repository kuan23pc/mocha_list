#GUI module for the task manager application
# Allowing users to manage tasks visually instead of using the CLI
import tkinter as tk
import tkinter.font as tkfont
from tkinter import simpledialog, messagebox, ttk
from datetime import datetime
from main import tasks, save_tasks

#Global state variables used for filtering and list navigation
current_filter = "all"
current_list_index = 0

#Data helper func.:

#Ensures that task data follows the expected structure
def normalize_data():
    global current_list_index

    # if tasks are in old format, convert to a default list structure
    if len(tasks) > 0 and "title" in tasks[0] and "completed" in tasks[0]:
        old_tasks = tasks[:] # Copy existing tasks
        tasks.clear() # Clear current structure
        tasks.append({ # Wrap old tasks into a default list structure
            "title": "My List",
            "tasks": old_tasks
        })

    # Ensure each list has required structure
    for task_list in tasks:
        # Add deault title if missing
        if "title" not in task_list:
            task_list["title"] = "Untitled List"
        # Ensure tasks key exists and is not a list
        if "tasks" not in task_list or not isinstance(task_list["tasks"], list):
            task_list["tasks"] = []
        # Validate each individual task
        for task in task_list["tasks"]:
            if "title" not in task:
                task["title"] = "Untitled Task" # set deafult title if missing
            if "completed" not in task:
                task["completed"] = False # ensure completed status exists
            if "deadline" not in task:
                task["deadline"] = None # ensure deadline field exists
            if "description" not in task:
                task["description"] = "" # ensure description field exists

    #Adjust current list index to stay within bounds
    if len(tasks) == 0:
        current_list_index = -1
    elif current_list_index >= len(tasks):
        current_list_index = len(tasks) - 1 # move to last vaild index 

#returns tasks from the currently selected list
def get_current_tasks():
    if current_list_index == -1 or not tasks:
        return []
    return tasks[current_list_index]["tasks"] # return tasks of active list

#Returns the title of the currently selected list
def get_current_list_title():
    if current_list_index == -1 or not tasks:
        return "No List Selected"
    return tasks[current_list_index]["title"] # Return active list title


# Placeholder config. for input field
PLACEHOLDER_TEXT = "Add a new task..."
PLACEHOLDER_COLOR = "#d87093"
NORMAL_ENTRY_COLOR = "black"

# Insert placeholder text if input field is empty
def set_placeholder():
    if entry.get() == "":
        entry.insert(0, PLACEHOLDER_TEXT)
        entry.config(fg=PLACEHOLDER_COLOR)

# Clears placeholder text when user starts typing
def clear_placeholder(event=None):
    if entry.cget("fg") == PLACEHOLDER_COLOR and entry.get() == PLACEHOLDER_TEXT:
        entry.delete(0, tk.END) # Remove placeholder text
        entry.config(fg=NORMAL_ENTRY_COLOR) # restore normal text color

# restores placeholder if input field is left empty
def restore_placeholder(event=None):
    if entry.get().strip() == "":
        entry.delete(0, tk.END) # clear whitespaces
        set_placeholder() # reinsert placeholder text

# Ensures placeholder disapperas correctly when typing begins
def handle_placeholder_typing(event):
    if entry.cget("fg") == PLACEHOLDER_COLOR and entry.get() == PLACEHOLDER_TEXT:
        entry.delete(0, tk.END) # remove placeholder text
        entry.config(fg=NORMAL_ENTRY_COLOR) # switch to normal text color


# Light effect for add task button to give visual feedback
def flash_add_button():
    original_bg = add_button.cget("bg")
    original_active_bg = add_button.cget("activebackground")
    add_button.config(bg="#fff4a3", activebackground="#fff4a3") # change color to highlight button
    root.after(180, lambda: add_button.config(bg=original_bg, activebackground=original_active_bg)) # restore original colors after short delay

# Validates deadline input (format and future date)
def validate_deadline(deadline_text):
    if deadline_text == "":
        return True, None

    # check correct date format
    try:
        parsed_deadline = datetime.strptime(deadline_text, "%Y-%m-%d").date()
    except ValueError:
        return False, "Please enter a valid date in YYYY-MM-DD format."

    # Ensures deadline is not in the past
    today = datetime.today().date()
    if parsed_deadline < today:
        return False, "Please enter a valid date that has not passed."

    return True, None


#Sidebar list functions, selects a list from the sidebar and refreshes UI
def select_list(index):
    global current_list_index
    if 0 <= index < len(tasks): # ensure index is within vaild tange
        current_list_index = index # update selected list
        refresh_all() 
# create a new list via user input
def create_new_list():
    title = simpledialog.askstring("New List", "Enter list title:")
    if title is None:
        return

    title = title.strip() # prevent empty list titles
    if title == "":
        messagebox.showerror("Invalid title", "List title cannot be empty.")
        return
    # Add new list structure
    tasks.append({
        "title": title,
        "tasks": []
    })
    save_tasks()
    # set new list as current active list
    global current_list_index
    current_list_index = len(tasks) - 1
    refresh_all()

# Renames the currenly selected list
def rename_current_list():
    if not tasks or current_list_index == -1: # check if a list is selected
        messagebox.showinfo("Rename List", "There is no list to rename.")
        return
    # get current title and prompt user for new title
    current_title = tasks[current_list_index]["title"]
    new_title = simpledialog.askstring("Rename List", "Enter new list title:", initialvalue=current_title)
    if new_title is None:
        return

    new_title = new_title.strip()
    # Prevent empty titles
    if new_title == "":
        messagebox.showerror("Invalid title", "List title cannot be empty.")
        return

    tasks[current_list_index]["title"] = new_title
    save_tasks()
    refresh_all()

# Deleted the currenly selected list
def delete_current_list():
    global current_list_index

    if not tasks or current_list_index == -1:
        messagebox.showinfo("Delete List", "There are no lists to delete.")
        return

    title = tasks[current_list_index]["title"]
    #Ask user for confirmation
    confirm = messagebox.askyesno
    ("Delete List", 
     f"Are you sure you want to delete the list '{title}'?"
    )
    if not confirm:
        return

    tasks.pop(current_list_index)

    #Adjust index after deletion
    if len(tasks) == 0:
        current_list_index = -1
    elif current_list_index >= len(tasks):
        current_list_index = len(tasks) - 1

    save_tasks()
    refresh_all()


# Filter functions, sets active filter (all/active/completed)
def set_filter(filter_name):
    global current_filter
    current_filter = filter_name
    refresh_all()

# Updates filter button styles vased on selected filter
def update_filter_buttons():
    active_bg = "#f4a6c1"
    inactive_bg = "#ffb6c1"

    all_button.config(bg=active_bg if current_filter == "all" else inactive_bg)
    active_button.config(bg=active_bg if current_filter == "active" else inactive_bg)
    completed_button.config(bg=active_bg if current_filter == "completed" else inactive_bg)

# Each item includes the original index and the task itself. 
def get_filtered_tasks():
    filtered = []
    current_tasks = get_current_tasks()

    for index, task in enumerate(current_tasks):
        if current_filter == "all": #Show all tasks
            filtered.append((index, task))
        elif current_filter == "active" and not task["completed"]:
            filtered.append((index, task)) #Show only active tasks
        elif current_filter == "completed" and task["completed"]:
            filtered.append((index, task)) #Show only completed tasks
    return filtered


# counter/progress/title, updates task statistics and progress bar
def update_counter():
    current_tasks = get_current_tasks()
    total = len(current_tasks)
    completed = sum(1 for task in current_tasks if task["completed"])
    remaining = total - completed
    
    #Update text label with task counts
    counter_label.config(
        text=f"Total: {total}    Completed: {completed}    Remaining: {remaining}"
    )
    #Calculate completion %
    percent = 0 if total == 0 else round((completed / total) * 100)
    progress_label.config(text=f"Progress: {percent}%")
    progress_bar["value"] = percent

# Updates the title of the currenly selected list
def update_main_title():
    list_title_label.config(text=get_current_list_title())


# Task functions, toggles task completion status when checkbar is clicked
def toggle_task(index, var):
    current_tasks = get_current_tasks()
    current_tasks[index]["completed"] = bool(var.get())
    save_tasks()
    refresh_all()

# Deletes a task after confirmation
def delete_task_gui(index):
    current_tasks = get_current_tasks()

    confirm = messagebox.askyesno(
        "Delete Task",
        f"Are you sure you want to delete '{current_tasks[index]['title']}'?"
    )
    if not confirm:
        return

    current_tasks.pop(index)
    save_tasks()
    refresh_all()

# Removes all completed tasks from the current list
def clear_completed_gui():
    if current_list_index == -1 or not tasks:
        messagebox.showinfo("Clear Completed", "There is no list selected.")
        return

    current_tasks = get_current_tasks()
    completed_tasks = [task for task in current_tasks if task["completed"]]

    #If no completed tasks exists
    if not completed_tasks:
        messagebox.showinfo("Clear Completed", "There are no completed tasks to remove.")
        return

    confirm = messagebox.askyesno(
        "Clear Completed",
        f"Are you sure you want to remove {len(completed_tasks)} completed task(s)?"
    )
    if not confirm:
        return

   # Keep only tasks that are not completed
    current_tasks[:] = [task for task in current_tasks if not task["completed"]]
    save_tasks()
    refresh_all()

# Opens a new window to edit tasks details
def open_edit_window(index):
    current_tasks = get_current_tasks()
    task = current_tasks[index]

    #Pop up window
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Task")
    edit_window.geometry("560x470")
    edit_window.configure(bg="#ffd9e8")
    edit_window.grab_set()
    edit_window.resizable(False, False)
    
    # Task title
    title_label = tk.Label(
        edit_window,
        text="Task Name",
        bg="#ffd9e8",
        fg="black",
        font=("Times New Roman", 14, "bold")
    )
    title_label.pack(anchor="w", padx=20, pady=(20, 5))


    title_entry = tk.Entry(
        edit_window,
        font=("Times New Roman", 13),
        width=40
    )
    title_entry.pack(padx=20, fill="x")
    title_entry.insert(0, task["title"])

    # Deadline
    deadline_label = tk.Label(
        edit_window,
        text="Deadline (YYYY-MM-DD)",
        bg="#ffd9e8",
        fg="black",
        font=("Times New Roman", 14, "bold")
    )
    deadline_label.pack(anchor="w", padx=20, pady=(15, 5))

    deadline_entry = tk.Entry(
        edit_window,
        font=("Times New Roman", 13),
        width=40
    )
    deadline_entry.pack(padx=20, fill="x")
    deadline_entry.insert(0, task.get("deadline") or "")

    description_label = tk.Label(   #Description
        edit_window,
        text="Description",
        bg="#ffd9e8",
        fg="black",
        font=("Times New Roman", 14, "bold")
    )
    description_label.pack(anchor="w", padx=20, pady=(15, 5))

    description_text = tk.Text(
        edit_window,
        font=("Times New Roman", 13),
        height=7,
        width=40
    )
    description_text.pack(padx=20, fill="both")
    description_text.insert("1.0", task.get("description", ""))

    # Save edited values
    def save_edit():
        new_title = title_entry.get().strip()
        new_deadline = deadline_entry.get().strip()
        new_description = description_text.get("1.0", tk.END).strip()

       #Validate title/deadline
        if new_title == "":
            messagebox.showerror("Invalid task", "Task name cannot be empty.", parent=edit_window)
            return

        is_valid, error_message = validate_deadline(new_deadline)
        if not is_valid:
            messagebox.showerror("Invalid date", error_message, parent=edit_window)
            return

        #Update task data
        task["title"] = new_title
        task["deadline"] = new_deadline if new_deadline != "" else None
        task["description"] = new_description

        save_tasks()
        edit_window.destroy()
        refresh_all()

    # Button container
    button_frame = tk.Frame(edit_window, bg="#ffd9e8")
    button_frame.pack(pady=20)

    # Button to save changes made in edit window
    save_button = tk.Button(
        button_frame,
        text="Save Changes",
        command=save_edit,
        bg="#ffb6c1",
        fg="black",
        activebackground="#ff9eb5",
        font=("Times New Roman", 12),
        width=14
    )
    save_button.pack(side="left", padx=8)
    
    # Button to cancel editing and close window
    cancel_button = tk.Button(
        button_frame,
        text="Cancel",
        command=edit_window.destroy,
        bg="#ffb6c1",
        fg="black",
        activebackground="#ff9eb5",
        font=("Times New Roman", 12),
        width=10
    )
    cancel_button.pack(side="left", padx=8)

# Sets/updates a deadline for a specific task via dialog input
def set_deadline_gui(index):
    current_tasks = get_current_tasks()

    deadline = simpledialog.askstring("Deadline", "Enter deadline (YYYY-MM-DD):")
    if deadline is None:
        return

    deadline = deadline.strip()

    #Validate deadline format and value
    is_valid, error_message = validate_deadline(deadline)
    if not is_valid:
        messagebox.showerror("Invalid date", error_message)
        return

    current_tasks[index]["deadline"] = deadline if deadline != "" else None
    save_tasks()
    refresh_all()

# Adds a new task from GUI input field
def add_task_gui():
    # Ensures a list is selected
    if current_list_index == -1 or not tasks:
        messagebox.showerror("No List", "Create a list before adding a task.")
        return
    
    raw_text = entry.get()

    if entry.cget("fg") == PLACEHOLDER_COLOR and raw_text == PLACEHOLDER_TEXT:
        return

    task_title = raw_text.strip() #Prevent empty task titles
    if task_title == "":
        return

    # Add new task to currect list
    current_tasks = get_current_tasks()
    current_tasks.append({
        "title": task_title,
        "completed": False,
        "deadline": None,
        "description": ""
    })
    save_tasks()

    #reset input field and restore placeholder
    entry.delete(0, tk.END)
    entry.config(fg=NORMAL_ENTRY_COLOR)
    set_placeholder()

    flash_add_button() #Visual feedback and UI refresh
    refresh_all()

def add_task_with_enter(event): #Allows pressing enter to add a task
    add_task_gui()


# Refresh UI
def refresh_sidebar():
    for widget in sidebar_lists_frame.winfo_children():
        widget.destroy()

    # Show message if no lists exists
    if not tasks:
        empty_label = tk.Label(
            sidebar_lists_frame,
            text="No lists yet",
            bg="#f6bfd2",
            fg="black",
            font=("Times New Roman", 12, "italic")
        )
        empty_label.pack(padx=8, pady=8, anchor="w")
        return

    # creates buttons for each list
    for index, task_list in enumerate(tasks):
        bg_color = "#f4a6c1" if index == current_list_index else "#ffb6c1"


        list_button = tk.Button(
            sidebar_lists_frame,
            text=task_list["title"],
            command=lambda i=index: select_list(i),
            bg=bg_color,
            fg="black",
            activebackground="#ff9eb5",
            font=("Times New Roman", 12),
            width=18,
            anchor="w"
        )
        list_button.pack(fill="x", padx=8, pady=4)

# Updates the task display area
def refresh_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    filtered_tasks = get_filtered_tasks()
    # Show message if no tasks/no matches
    if not filtered_tasks:
        current_tasks = get_current_tasks()
        empty_text = "Add your first task above!" if len(current_tasks) == 0 else "No tasks match this filter."


        empty_label = tk.Label(
            tasks_frame,
            text=empty_text,
            bg="#ffd9e8",
            fg="#c71565",
            font=("Times New Roman", 16, "italic"),
            pady=30
        )
        empty_label.pack()

    else:
        # Create UI rows for each task
        for real_index, task in filtered_tasks:
            row = tk.Frame(
                tasks_frame,
                bg="#ffe4ee",
                bd=1,
                relief="solid",
                padx=12,
                pady=10
            )
            row.pack(fill="x", padx=20, pady=8)

            left_frame = tk.Frame(row, bg="#ffe4ee")
            left_frame.pack(side="left", fill="x", expand=True)
            #track checkbox state
            completed_var = tk.IntVar(value=1 if task["completed"] else 0)

            top_line = tk.Frame(left_frame, bg="#ffe4ee")
            top_line.pack(fill="x", pady=(0, 4))

            # Checkbox for completion toggle
            # When clicked, it updates the task's "completed" field via toggle_task
            checkbox = tk.Checkbutton(
                top_line,
                variable=completed_var,
                command=lambda i=real_index, v=completed_var: toggle_task(i, v),
                bg="#ffe4ee",
                activebackground="#ffe4ee",
                selectcolor="white",
                bd=0,
                highlightthickness=0
            )
            checkbox.pack(side="left", padx=(0, 8))

            # Visual status indicator if the task is completed/not
            status_symbol = "✔" if task["completed"] else "✗"
            status_color = "green" if task["completed"] else "#c71565"

            status_label = tk.Label(
                top_line,
                text=status_symbol,
                fg=status_color,
                bg="#ffe4ee",
                font=("Times New Roman", 16, "bold"),
                width=2
            )
            status_label.pack(side="left", padx=(0, 8))

            task_font = completed_font if task["completed"] else normal_font

            task_label = tk.Label(
                top_line,
                text=task["title"],
                fg="black",
                bg="#ffe4ee",
                font=task_font,
                anchor="w"
            )
            task_label.pack(side="left", fill="x", expand=True)
            
            # Show deadline if it exists
            deadline = task.get("deadline")
            if deadline:
                deadline_label = tk.Label(
                    left_frame,
                    text=f"Deadline: {deadline}",
                    fg="#8b0f4d",
                    bg="#ffe4ee",
                    font=("Times New Roman", 11, "italic"),
                    anchor="w"
                )
                deadline_label.pack(fill="x", padx=(40, 0), pady=(2, 0))
 

            description = task.get("description", "").strip()
            if description:
                description_label = tk.Label(
                    left_frame,
                    text=f"Description: {description}",
                    fg="black",
                    bg="#ffe4ee",
                    font=("Times New Roman", 11),
                    anchor="w",
                    justify="left",
                    wraplength=420
                )
                description_label.pack(fill="x", padx=(40, 0), pady=(2, 0))

            # Action buttoms (edit, deadline, delete)
            button_frame = tk.Frame(row, bg="#ffe4ee")
            button_frame.pack(side="right", padx=(20, 0))


            edit_button = tk.Button(
                button_frame,
                text="Edit",
                command=lambda i=real_index: open_edit_window(i),
                bg="#ffb6c1",
                fg="black",
                activebackground="#ff9eb5",
                font=("Times New Roman", 10),
                width=8
            )
            edit_button.grid(row=0, column=0, padx=4, pady=2)


            deadline_button = tk.Button(
                button_frame,
                text="Set Deadline",
                command=lambda i=real_index: set_deadline_gui(i),
                bg="#ffb6c1",
                fg="black",
                activebackground="#ff9eb5",
                font=("Times New Roman", 10),
                width=12
            )
            deadline_button.grid(row=0, column=1, padx=4, pady=2)


            delete_button = tk.Button(
                button_frame,
                text="Delete",
                command=lambda i=real_index: delete_task_gui(i),
                bg="#ffb6c1",
                fg="black",
                activebackground="#ff9eb5",
                font=("Times New Roman", 10),
                width=8
            )
            delete_button.grid(row=0, column=2, padx=4, pady=2)


def refresh_all():
    refresh_sidebar()
    refresh_tasks()
    update_counter()
    update_filter_buttons()
    update_main_title()


# GUI setup

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("mochalist.app.1.0")
# Set a custom app ID for Windows so the app can use its own icon properly

normalize_data()
# Make sure the task data is in the correct format before the GUI starts

root = tk.Tk()
# Create the main window

# Try to load and set the app icon
try:
    icon_image = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon_image)
except Exception:
    pass

# Main window settings
root.title("Mocha List")
root.geometry("1220x760")
root.configure(bg="#ffd9e8")

# Progress bar style
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Pink.Horizontal.TProgressbar",
    troughcolor="#ffe4ee",
    background="#c71565",
    bordercolor="#ffe4ee",
    lightcolor="#c71565",
    darkcolor="#c71565"
)

# Fonts for normal and completed tasks
normal_font = tkfont.Font(family="Times New Roman", size=15)
completed_font = tkfont.Font(family="Times New Roman", size=15, overstrike=1)

# Main container holds sidebar and main content area
main_container = tk.Frame(root, bg="#ffd9e8")
main_container.pack(fill="both", expand=True)


# Sidebar
sidebar = tk.Frame(main_container, bg="#f6bfd2", width=250)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


sidebar_title = tk.Label(
    sidebar,
    text="Lists",
    bg="#f6bfd2",
    fg="#c71565",
    font=("Times New Roman", 22, "bold italic")
)
sidebar_title.pack(pady=(20, 10))


# Buttons for creating, renaming, and deleting lists
new_list_button = tk.Button(
    sidebar,
    text="New List",
    command=create_new_list,
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 12),
    width=18
)
new_list_button.pack(pady=5)


rename_list_button = tk.Button(
    sidebar,
    text="Rename List",
    command=rename_current_list,
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 12),
    width=18
)
rename_list_button.pack(pady=5)


delete_list_button = tk.Button(
    sidebar,
    text="Delete List",
    command=delete_current_list,
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 12),
    width=18
)
delete_list_button.pack(pady=(5, 15))


# Frame where the available lists will be displayed
sidebar_lists_frame = tk.Frame(sidebar, bg="#f6bfd2")
sidebar_lists_frame.pack(fill="both", expand=True, padx=8, pady=8)

# Main content area where tasks and controls are shown
content = tk.Frame(main_container, bg="#ffd9e8")
content.pack(side="left", fill="both", expand=True)

title_label = tk.Label(
    content,
    text="Mocha List",
    bg="#ffd9e8",
    fg="#c71565",
    font=("Times New Roman", 30, "bold italic")
)
title_label.pack(pady=(20, 8))

# Shows the currently selected list name
list_title_label = tk.Label(
    content,
    text="",
    bg="#ffd9e8",
    fg="#8b0f4d",
    font=("Times New Roman", 22, "bold")
)
list_title_label.pack(pady=(0, 8))

# Shows task counters such as total/completed/remaining
counter_label = tk.Label(
    content,
    text="",
    bg="#ffd9e8",
    fg="black",
    font=("Times New Roman", 15, "bold")
)
counter_label.pack(pady=(0, 10))

# Shows progress in text form
progress_label = tk.Label(
    content,
    text="Progress: 0%",
    bg="#ffd9e8",
    fg="black",
    font=("Times New Roman", 13, "bold")
)
progress_label.pack(pady=(0, 6))


# Progress bar for completed tasks
progress_bar = ttk.Progressbar(
    content,
    style="Pink.Horizontal.TProgressbar",
    orient="horizontal",
    length=320,
    mode="determinate"
)
progress_bar.pack(pady=(0, 16))

# Top frame contains task input and action buttons
top_frame = tk.Frame(content, bg="#ffd9e8")
top_frame.pack(pady=10)

# Entry box for typing a new task
entry = tk.Entry(
    top_frame,
    width=32,
    font=("Times New Roman", 15),
    bd=2,
    relief="solid",
    fg=NORMAL_ENTRY_COLOR
)
entry.pack(side="left", padx=8, ipady=6)
entry.bind("<Return>", add_task_with_enter)  # Add task when Enter is pressed
entry.bind("<FocusIn>", clear_placeholder)  # Remove placeholder when entry gets focus
entry.bind("<FocusOut>", restore_placeholder)   # Restore placeholder if entry is empty
entry.bind("<KeyPress>", handle_placeholder_typing)


# Button to add a new task
add_button = tk.Button(
    top_frame,
    text="Add Task",
    command=add_task_gui,
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 12),
    width=12
)
add_button.pack(side="left", padx=8, ipadx=6, ipady=4)


# Button to remove all completed tasks
clear_completed_button = tk.Button(
    top_frame,
    text="Clear Completed",
    command=clear_completed_gui,
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 12),
    width=15
)
clear_completed_button.pack(side="left", padx=8, ipadx=6, ipady=4)


# Filter section for showing all, active, or completed tasks
filter_frame = tk.Frame(content, bg="#ffd9e8")
filter_frame.pack(pady=(8, 16))


all_button = tk.Button(
    filter_frame,
    text="All",
    command=lambda: set_filter("all"),
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 11),
    width=10
)
all_button.pack(side="left", padx=6)


active_button = tk.Button(
    filter_frame,
    text="Active",
    command=lambda: set_filter("active"),
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 11),
    width=10
)
active_button.pack(side="left", padx=6)


completed_button = tk.Button(
    filter_frame,
    text="Completed",
    command=lambda: set_filter("completed"),
    bg="#ffb6c1",
    fg="black",
    activebackground="#ff9eb5",
    font=("Times New Roman", 11),
    width=10
)
completed_button.pack(side="left", padx=6)


# Main area for the scrollable task list
main_list_frame = tk.Frame(content, bg="#ffd9e8")
main_list_frame.pack(fill="both", expand=True, padx=20, pady=10)

# New container for canvas + scrollbars
scroll_frame = tk.Frame(main_list_frame, bg="#ffd9e8")
scroll_frame.pack(fill="both", expand=True)

# Canvas + scrollbar setup makes the task list scrollable
canvas = tk.Canvas(scroll_frame, bg="#ffd9e8", highlightthickness=0)

# Vertical Scrollbar
vertical_scrollbar = tk.Scrollbar(
    scroll_frame,
    orient = "vertical",
)

# Horizontal scrollbar
horizontal_scrollbar = tk.Scrollbar(
    scroll_frame,
    orient = "horizontal",
)
#Frame inside canvas that holds all task widgets
tasks_frame = tk.Frame(canvas, bg="#ffd9e8")

# Update the scroll area whenever the task frame changes size
def update_scrollregion(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

tasks_frame.bind("<Configure>", update_scrollregion)

# Mouse wheel scrolling
def _on_mousewheel_windows(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Scroll up on Linux
def _on_mousewheel_linux_up(event):
    canvas.yview_scroll(-1, "units")

# Scroll down on Linux
def _on_mousewheel_linux_down(event):
    canvas.yview_scroll(1, "units")

# Add mouse wheel scrolling to a widget and all its child widgets
def bind_mousewheel(widget):
    widget.bind("<MouseWheel>", _on_mousewheel_windows)
    widget.bind("<Button-4>", _on_mousewheel_linux_up)
    widget.bind("<Button-5>", _on_mousewheel_linux_down)

    for child in widget.winfo_children():
        bind_mousewheel(child)


# Put the task frame inside the canvas and connect scrollbar
canvas_window = canvas.create_window(
    (0, 0), 
    window=tasks_frame, 
    anchor="nw")

vertical_scrollbar.config(command=canvas.yview)
horizontal_scrollbar.config(command=canvas.xview)

canvas.configure(
    yscrollcommand=vertical_scrollbar.set,
    xscrollcommand=horizontal_scrollbar.set
)

horizontal_scrollbar.pack(side = "bottom", fill = "x")
vertical_scrollbar.pack(side = "right", fill = "y")
canvas.pack(side="left", fill = "both", expand = True)

# Start with placeholder text and refresh the whole GUI
set_placeholder()
refresh_all()

# Enable scrolling in the task area
bind_mousewheel(canvas)
bind_mousewheel(tasks_frame)
bind_mousewheel(main_list_frame)

# Start the Tkinter event loop
root.mainloop()