# GUI module for the task manager application
# Allowing users to manage tasks visually instead of using the CLI
import tkinter as tk
import tkinter.font as tkfont
from tkinter import simpledialog, messagebox, ttk
from datetime import datetime
from main import tasks, save_tasks

# Global state variables used for filtering and list navigation
current_filter = "all"
current_list_index = 0

# Color themes for the GUI
# Current selected theme
current_theme = "Calm Breeze"

# Color themes for the GUI
THEMES = {
"Calm Breeze": {
    "bg": "#FFFCF8",
    "sidebar": "#EFD8CF",
    "row": "#FFFFFF",
    "button": "#E9D2C8",
    "button_active": "#DDBFB3",
    "selected": "#D8B8B2",
    "accent": "#A66F65",
    "accent_dark": "#6B4842",
    "text": "#2E2926",
    "muted": "#7D6E68",
    "placeholder": "#9A867F",
    "success": "#8DA383",
    "danger": "#A45F5F",
    "flash": "#FFF1B8",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#F4E5DE"
},

    "Cotton Candy": {
    "bg": "#FFF9FC",
    "sidebar": "#FFE4F0",
    "row": "#FFFFFF",
    "button": "#FFC4DD",
    "button_active": "#FFADCF",
    "selected": "#FFB8D6",
    "accent": "#E86FA8",
    "accent_dark": "#B94D7E",
    "text": "#2F2429",
    "muted": "#7A626B",
    "placeholder": "#A07988",
    "success": "#7FA86B",
    "danger": "#C94F72",
    "flash": "#FFADCF",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#FFEAF4"
},

    "Ocean Dream": {
    "bg": "#F4FBFD",
    "sidebar": "#B8E2F2",
    "row": "#FFFFFF",
    "button": "#A6D8EE",
    "button_active": "#8FCDE8",
    "selected": "#D0EFF9",
    "accent": "#72C5E8",
    "accent_dark": "#4A9FC4",
    "text": "#223036",
    "muted": "#667980",
    "placeholder": "#7D929A",
    "success": "#6FA878",
    "danger": "#A95F5F",
    "flash": "#A8D6FF",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#D0EFF9"
},

   "Matcha Cream": {
    "bg": "#FBFFF6",
    "sidebar": "#EAF4D8",
    "row": "#FFFFFF",
    "button": "#DDEDC2",
    "button_active": "#D0E3AD",
    "selected": "#C2D99B",
    "accent": "#8DAA5F",
    "accent_dark": "#657D3F",
    "text": "#2B3022",
    "muted": "#747D63",
    "placeholder": "#909B78",
    "success": "#7FA65A",
    "danger": "#A86A6A",
    "flash": "#FFF1A8",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#EEF6DE"
},

"Cherry Pie": {
    "bg": "#FFF5F5",
    "sidebar": "#DFA3AA",
    "row": "#FFFFFF",
    "button": "#D45D6C",
    "button_active": "#C94F5F",
    "selected": "#8F1D32",
    "accent": "#A1122B",
    "accent_dark": "#8F1D32",
    "text": "#2F1D20",
    "muted": "#7D5B60",
    "placeholder": "#9A747A",
    "success": "#7F9A68",
    "danger": "#B1122D",
    "flash": "#C94F5F",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#F0CDD2"
},

    "Lavender Bloom": {
    "bg": "#FBF7FF",
    "sidebar": "#E3CFF2",
    "row": "#FFFFFF",
    "button": "#D5B4EF",
    "button_active": "#C79BE8",
    "selected": "#B982E0",
    "accent": "#9C5FD1",
    "accent_dark": "#6F3FA0",
    "text": "#2D2433",
    "muted": "#74647D",
    "placeholder": "#8B7998",
    "success": "#7FA06B",
    "danger": "#B85C75",
    "flash": "#FFF1A8",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#EADAF6"
},

"Summer Pop": {
    "bg": "#FFFCEB",
    "sidebar": "#BDEFF2",
    "row": "#FFFFFF",
    "button": "#FFB3D1",
    "button_active": "#FF8FBE",
    "selected": "#F47CB4",
    "accent": "#69A957",
    "accent_dark": "#176A94",
    "text": "#2F2A24",
    "muted": "#6F7C78",
    "placeholder": "#7A8C88",
    "success": "#69A957",
    "danger": "#D94F7E",
    "flash": "#FED439",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#D8F6F8"
},


"Blank Canvas": {
    "bg": "#FFFFFF",
    "sidebar": "#FFFFFF",
    "row": "#FFFFFF",
    "button": "#FFFFFF",
    "button_active": "#F5F5F5",
    "selected": "#F0F0F0",
    "accent": "#222222",
    "accent_dark": "#000000",
    "text": "#222222",
    "muted": "#777777",
    "placeholder": "#999999",
    "success": "#222222",
    "danger": "#9B4A4A",
    "flash": "#FFF4B8",
    "entry_bg": "#FFFFFF",
    "progress_trough": "#F5F5F5"
},


    "Midnight Calm": {
        "bg": "#111827",
        "sidebar": "#1F2937",
        "row": "#273449",
        "button": "#374151",
        "button_active": "#4B5563",
        "selected": "#475569",
        "accent": "#A7C7E7",
        "accent_dark": "#DDEAFE",
        "text": "#F9FAFB",
        "muted": "#CBD5E1",
        "placeholder": "#94A3B8",
        "success": "#86EFAC",
        "danger": "#FCA5A5",
        "flash": "#586A85",
        "entry_bg": "#0F172A",
        "progress_trough": "#1F2937"
    }

}



def C(color_name):
    return THEMES[current_theme][color_name]

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

    # Adjust current list index to stay within bounds
    if len(tasks) == 0:
        current_list_index = -1
    elif current_list_index >= len(tasks):
        current_list_index = len(tasks) - 1 # move to last vaild index 

# returns tasks from the currently selected list
def get_current_tasks():
    if current_list_index == -1 or not tasks:
        return []
    return tasks[current_list_index]["tasks"] # return tasks of active list

# Returns the title of the currently selected list
def get_current_list_title():
    if current_list_index == -1 or not tasks:
        return "No List Selected"
    return tasks[current_list_index]["title"] # Return active list title


# Placeholder config. for input field
PLACEHOLDER_TEXT = "Add a new task..."
NORMAL_ENTRY_COLOR = "black"

# Insert placeholder text if input field is empty
def set_placeholder():
    if entry.get() == "":
        entry.insert(0, PLACEHOLDER_TEXT)
        entry.config(fg=C("placeholder"))

# Clears placeholder text when user starts typing
def clear_placeholder(event=None):
    if entry.cget("fg") == C("placeholder") and entry.get() == PLACEHOLDER_TEXT:
        entry.delete(0, tk.END) # Remove placeholder text
        entry.config(fg=C("text")) # restore normal text color

# restores placeholder if input field is left empty
def restore_placeholder(event=None):
    if entry.get().strip() == "":
        entry.delete(0, tk.END) # clear whitespaces
        set_placeholder() # reinsert placeholder text

# Ensures placeholder disapperas correctly when typing begins
def handle_placeholder_typing(event):
    if entry.cget("fg") == C("placeholder") and entry.get() == PLACEHOLDER_TEXT:
        entry.delete(0, tk.END) # remove placeholder text
        entry.config(fg=C("text")) # restore normal text color

# Light effect for add task button to give visual feedback
def flash_add_button():
    original_bg = add_button.cget("bg")
    original_active_bg = add_button.cget("activebackground")

    add_button.config(
        bg=C("button_active"),
        activebackground=C("button_active")
    )

    root.after(
        180,
        lambda: add_button.config(
            bg=original_bg,
            activebackground=original_active_bg
        )
    )

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


# Sidebar list functions, selects a list from the sidebar and refreshes UI
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

    confirm = messagebox.askyesno(
        "Delete List",
        f"Are you sure you want to delete the list '{title}'?"
    )

    if not confirm:
        return

    tasks.pop(current_list_index)

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
    all_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active"),
        relief="sunken" if current_filter == "all" else "raised"
    )

    active_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active"),
        relief="sunken" if current_filter == "active" else "raised"
    )

    completed_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active"),
        relief="sunken" if current_filter == "completed" else "raised"
    )

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

    counter_label.config(
        text=f"Total: {total}    Completed: {completed}    Remaining: {remaining}",
        bg=C("bg"),
        fg=C("text")
    )

    percent = 0 if total == 0 else round((completed / total) * 100)

    progress_label.config(
        text=f"Progress: {percent}%",
        bg=C("bg"),
        fg=C("text")
    )

    progress_bar["value"] = percent

# Updates the title of the currenly selected list
def update_main_title():
    list_title_label.config(
        text=get_current_list_title(),
        bg=C("bg"),
        fg=C("accent_dark")
    )


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

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Task")
    edit_window.geometry("560x470")
    edit_window.configure(bg=C("bg"))
    edit_window.grab_set()
    edit_window.resizable(False, False)

    title_label = tk.Label(
        edit_window,
        text="Task Name",
        bg=C("bg"),
        fg=C("text"),
        font=("Times New Roman", 14, "bold")
    )
    title_label.pack(anchor="w", padx=20, pady=(20, 5))

    title_entry = tk.Entry(
        edit_window,
        font=("Times New Roman", 13),
        width=40,
        bg=C("entry_bg"),
        fg=C("text"),
        insertbackground=C("text")
    )
    title_entry.pack(padx=20, fill="x")
    title_entry.insert(0, task["title"])

    deadline_label = tk.Label(
        edit_window,
        text="Deadline (YYYY-MM-DD)",
        bg=C("bg"),
        fg=C("text"),
        font=("Times New Roman", 14, "bold")
    )
    deadline_label.pack(anchor="w", padx=20, pady=(15, 5))

    deadline_entry = tk.Entry(
        edit_window,
        font=("Times New Roman", 13),
        width=40,
        bg=C("entry_bg"),
        fg=C("text"),
        insertbackground=C("text")
    )
    deadline_entry.pack(padx=20, fill="x")
    deadline_entry.insert(0, task.get("deadline") or "")

    description_label = tk.Label(
        edit_window,
        text="Description",
        bg=C("bg"),
        fg=C("text"),
        font=("Times New Roman", 14, "bold")
    )
    description_label.pack(anchor="w", padx=20, pady=(15, 5))

    description_text = tk.Text(
        edit_window,
        font=("Times New Roman", 13),
        height=7,
        width=40,
        bg=C("entry_bg"),
        fg=C("text"),
        insertbackground=C("text")
    )
    description_text.pack(padx=20, fill="both")
    description_text.insert("1.0", task.get("description", ""))

    def save_edit():
        new_title = title_entry.get().strip()
        new_deadline = deadline_entry.get().strip()
        new_description = description_text.get("1.0", tk.END).strip()

        if new_title == "":
            messagebox.showerror("Invalid task", "Task name cannot be empty.", parent=edit_window)
            return

        is_valid, error_message = validate_deadline(new_deadline)

        if not is_valid:
            messagebox.showerror("Invalid date", error_message, parent=edit_window)
            return

        task["title"] = new_title
        task["deadline"] = new_deadline if new_deadline != "" else None
        task["description"] = new_description

        save_tasks()
        edit_window.destroy()
        refresh_all()

    button_frame = tk.Frame(edit_window, bg=C("bg"))
    button_frame.pack(pady=20)

    save_button = tk.Button(
        button_frame,
        text="Save Changes",
        command=save_edit,
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active"),
        font=("Times New Roman", 12),
        width=14
    )
    save_button.pack(side="left", padx=8)

    cancel_button = tk.Button(
        button_frame,
        text="Cancel",
        command=edit_window.destroy,
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active"),
        font=("Times New Roman", 12),
        width=10
    )
    cancel_button.pack(side="left", padx=8)


##############################
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
    if current_list_index == -1 or not tasks:
        messagebox.showerror("No List", "Create a list before adding a task.")
        return

    raw_text = entry.get()

    if entry.cget("fg") == C("placeholder") and raw_text == PLACEHOLDER_TEXT:
        return

    task_title = raw_text.strip()

    if task_title == "":
        return

    current_tasks = get_current_tasks()
    current_tasks.append({
        "title": task_title,
        "completed": False,
        "deadline": None,
        "description": ""
    })

    save_tasks()

    entry.delete(0, tk.END)
    entry.config(fg=C("text"))
    set_placeholder()

    flash_add_button()
    refresh_all()

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
            bg=C("sidebar"),
            fg=C("muted"),
            font=("Times New Roman", 12, "italic")
        )
        empty_label.pack(padx=8, pady=8, anchor="w")
        return

    # Creates buttons for each list
    for index, task_list in enumerate(tasks):
        bg_color = C("button")
        list_button = tk.Button (
            sidebar_lists_frame,
            text=task_list["title"],
            command=lambda i=index: select_list(i),
            bg=bg_color,
            fg=C("text"),
            activebackground=C("button_active"),
            font=("Times New Roman", 12),
            width=18,
            anchor="w",
            relief="sunken" if index == current_list_index else "raised"

        )
        list_button.pack(fill="x", padx=8, pady=4)
        
# Updates the task display area
def refresh_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    filtered_tasks = get_filtered_tasks()

    if not filtered_tasks:
        current_tasks = get_current_tasks()
        empty_text = "Add your first task above!" if len(current_tasks) == 0 else "No tasks match this filter."

        empty_label = tk.Label(
            tasks_frame,
            text=empty_text,
            bg=C("bg"),
            fg=C("accent"),
            font=("Times New Roman", 16, "italic"),
            pady=30
        )
        empty_label.pack()

    else:
        for real_index, task in filtered_tasks:
            row = tk.Frame(
                tasks_frame,
                bg=C("row"),
                bd=1,
                relief="solid",
                padx=12,
                pady=10
            )
            row.pack(fill="x", padx=20, pady=8)

            left_frame = tk.Frame(row, bg=C("row"))
            left_frame.pack(side="left", fill="x", expand=True)

            completed_var = tk.IntVar(value=1 if task["completed"] else 0)

            top_line = tk.Frame(left_frame, bg=C("row"))
            top_line.pack(fill="x", pady=(0, 4))

            checkbox = tk.Checkbutton(
                top_line,
                variable=completed_var,
                command=lambda i=real_index, v=completed_var: toggle_task(i, v),
                bg=C("row"),
                activebackground=C("row"),
                selectcolor=C("entry_bg"),
                bd=0,
                highlightthickness=0
            )
            checkbox.pack(side="left", padx=(0, 8))

            status_symbol = "✔" if task["completed"] else "✗"
            status_color = C("success") if task["completed"] else C("danger")

            status_label = tk.Label(
                top_line,
                text=status_symbol,
                fg=status_color,
                bg=C("row"),
                font=("Times New Roman", 16, "bold"),
                width=2
            )
            status_label.pack(side="left", padx=(0, 8))

            task_font = completed_font if task["completed"] else normal_font

            task_label = tk.Label(
                top_line,
                text=task["title"],
                fg=C("text"),
                bg=C("row"),
                font=task_font,
                anchor="w"
            )
            task_label.pack(side="left", fill="x", expand=True)

            deadline = task.get("deadline")

            if deadline:
                deadline_label = tk.Label(
                    left_frame,
                    text=f"Deadline: {deadline}",
                    fg=C("accent_dark"),
                    bg=C("row"),
                    font=("Times New Roman", 11, "italic"),
                    anchor="w"
                )
                deadline_label.pack(fill="x", padx=(40, 0), pady=(2, 0))

            description = task.get("description", "").strip()

            if description:
                description_label = tk.Label(
                    left_frame,
                    text=f"Description: {description}",
                    fg=C("text"),
                    bg=C("row"),
                    font=("Times New Roman", 11),
                    anchor="w",
                    justify="left",
                    wraplength=420
                )
                description_label.pack(fill="x", padx=(40, 0), pady=(2, 0))

            button_frame = tk.Frame(row, bg=C("row"))
            button_frame.pack(side="right", padx=(20, 0))

            edit_button = tk.Button(
                button_frame,
                text="Edit",
                command=lambda i=real_index: open_edit_window(i),
                bg=C("button"),
                fg=C("text"),
                activebackground=C("button_active"),
                font=("Times New Roman", 10),
                width=8
            )
            edit_button.grid(row=0, column=0, padx=4, pady=2)

            deadline_button = tk.Button(
                button_frame,
                text="Set Deadline",
                command=lambda i=real_index: set_deadline_gui(i),
                bg=C("button"),
                fg=C("text"),
                activebackground=C("button_active"),
                font=("Times New Roman", 10),
                width=12
            )
            deadline_button.grid(row=0, column=1, padx=4, pady=2)

            delete_button = tk.Button(
                button_frame,
                text="Delete",
                command=lambda i=real_index: delete_task_gui(i),
                bg=C("button"),
                fg=C("text"),
                activebackground=C("button_active"),
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

def change_theme(selected_theme):
    global current_theme
    current_theme = selected_theme
    apply_theme()


def apply_theme():
    root.configure(bg=C("bg"))

    style.configure(
        "Theme.Horizontal.TProgressbar",
        troughcolor=C("progress_trough"),
        background=C("accent"),
        bordercolor=C("progress_trough"),
        lightcolor=C("accent"),
        darkcolor=C("accent")
    )

    main_container.config(bg=C("bg"))

    sidebar.config(bg=C("sidebar"))
    sidebar_title.config(bg=C("sidebar"), fg=C("accent"))

    new_list_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active")
    )

    rename_list_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active")
    )

    delete_list_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active")
    )

    theme_label.config(
        bg=C("sidebar"),
        fg=C("accent")
    )

    theme_menu.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active"),
        highlightbackground=C("sidebar")
    )

    theme_menu["menu"].config(
        bg=C("entry_bg"),
        fg=C("text")
    )

    sidebar_lists_frame.config(bg=C("sidebar"))

    content.config(bg=C("bg"))
    title_label.config(bg=C("bg"), fg=C("accent"))
    list_title_label.config(bg=C("bg"), fg=C("accent_dark"))
    counter_label.config(bg=C("bg"), fg=C("text"))
    progress_label.config(bg=C("bg"), fg=C("text"))

    top_frame.config(bg=C("bg"))

    if entry.get() == PLACEHOLDER_TEXT:
        entry.config(
            bg=C("entry_bg"),
            fg=C("placeholder"),
            insertbackground=C("text")
        )
    else:
        entry.config(
            bg=C("entry_bg"),
            fg=C("text"),
            insertbackground=C("text")
        )

    add_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active")
    )

    clear_completed_button.config(
        bg=C("button"),
        fg=C("text"),
        activebackground=C("button_active")
    )

    filter_frame.config(bg=C("bg"))

    main_list_frame.config(bg=C("bg"))
    canvas.config(bg=C("bg"))
    tasks_frame.config(bg=C("bg"))

    refresh_all()


# GUI setup

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("calmlist.app.1.0")
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
root.title("CALM List")
root.geometry("1220x760")
root.configure(bg=C("bg"))


# Progress bar style
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Theme.Horizontal.TProgressbar",
    troughcolor=C("progress_trough"),
    background=C("accent"),
    bordercolor=C("progress_trough"),
    lightcolor=C("accent"),
    darkcolor=C("accent")
)


# Fonts for normal and completed tasks
normal_font = tkfont.Font(family="Times New Roman", size=15)
completed_font = tkfont.Font(family="Times New Roman", size=15, overstrike=1)

# Main container holds sidebar and main content area
main_container = tk.Frame(root, bg=C("bg"))
main_container.pack(fill="both", expand=True)


# Sidebar
sidebar = tk.Frame(main_container, bg=C("sidebar"), width=250)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


sidebar_title = tk.Label(
    sidebar,
    text="Lists",
    bg=C("sidebar"),
    fg=C("accent"),
    font=("Times New Roman", 22, "bold italic")
)
sidebar_title.pack(pady=(20, 10))


# Buttons for creating, renaming, and deleting lists
new_list_button = tk.Button(
    sidebar,
    text="New List",
    command=create_new_list,
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 12),
    width=18
)
new_list_button.pack(pady=5)


rename_list_button = tk.Button(
    sidebar,
    text="Rename List",
    command=rename_current_list,
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 12),
    width=18
)
rename_list_button.pack(pady=5)


delete_list_button = tk.Button(
    sidebar,
    text="Delete List",
    command=delete_current_list,
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 12),
    width=18
)

delete_list_button.pack(pady=(5, 15))

# Theme selector
theme_label = tk.Label(
    sidebar,
    text="Theme",
    bg=C("sidebar"),
    fg=C("accent"),
    font=("Times New Roman", 12, "bold")
)
theme_label.pack(pady=(5, 2))

theme_var = tk.StringVar(value=current_theme)

theme_menu = tk.OptionMenu(
    sidebar,
    theme_var,
    *THEMES.keys(),
    command=change_theme
)
theme_menu.config(
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 11),
    width=16,
    highlightthickness=0
)
theme_menu["menu"].config(
    bg=C("entry_bg"),
    fg=C("text")
)
theme_menu.pack(pady=(0, 15))


# Frame where the available lists will be displayed
sidebar_lists_frame = tk.Frame(sidebar, bg=C("sidebar"))
sidebar_lists_frame.pack(fill="both", expand=True, padx=8, pady=8)

# Main content area where tasks and controls are shown
content = tk.Frame(main_container, bg=C("bg"))
content.pack(side="left", fill="both", expand=True)

title_label = tk.Label(
    content,
    text="Mocha List",
    bg=C("bg"),
    fg=C("accent"),
    font=("Times New Roman", 30, "bold italic")
)
title_label.pack(pady=(20, 8))

# Shows the currently selected list name
list_title_label = tk.Label(
    content,
    text="",
    bg=C("bg"),
    fg=C("accent_dark"),
    font=("Times New Roman", 22, "bold")
)
list_title_label.pack(pady=(0, 8))

# Shows task counters such as total/completed/remaining
counter_label = tk.Label(
    content,
    text="",
    bg=C("bg"),
    fg=C("text"),
    font=("Times New Roman", 15, "bold")
)
counter_label.pack(pady=(0, 10))

# Shows progress in text form
progress_label = tk.Label(
    content,
    text="Progress: 0%",
    bg=C("bg"),
    fg=C("text"),
    font=("Times New Roman", 13, "bold")
)
progress_label.pack(pady=(0, 6))


# Progress bar for completed tasks
progress_bar = ttk.Progressbar(
    content,
    style="Theme.Horizontal.TProgressbar",
    orient="horizontal",
    length=320,
    mode="determinate"
)
progress_bar.pack(pady=(0, 16))

# Top frame contains task input and action buttons
top_frame = tk.Frame(content, bg=C("bg"))
top_frame.pack(pady=10)

# Entry box for typing a new task
entry = tk.Entry(
    top_frame,
    width=32,
    font=("Times New Roman", 15),
    bd=2,
    relief="solid",
    bg=C("entry_bg"),
    fg=C("text"),
    insertbackground=C("text")
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
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 12),
    width=12
)
add_button.pack(side="left", padx=8, ipadx=6, ipady=4)


# Button to remove all completed tasks
clear_completed_button = tk.Button(
    top_frame,
    text="Clear Completed",
    command=clear_completed_gui,
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 12),
    width=15
)
clear_completed_button.pack(side="left", padx=8, ipadx=6, ipady=4)


# Filter section for showing all, active, or completed tasks
filter_frame = tk.Frame(content, bg=C("bg"))
filter_frame.pack(pady=(8, 16))


all_button = tk.Button(
    filter_frame,
    text="All",
    command=lambda: set_filter("all"),
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 11),
    width=10
)
all_button.pack(side="left", padx=6)


active_button = tk.Button(
    filter_frame,
    text="Active",
    command=lambda: set_filter("active"),
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 11),
    width=10
)
active_button.pack(side="left", padx=6)


completed_button = tk.Button(
    filter_frame,
    text="Completed",
    command=lambda: set_filter("completed"),
    bg=C("button"),
    fg=C("text"),
    activebackground=C("button_active"),
    font=("Times New Roman", 11),
    width=10
)
completed_button.pack(side="left", padx=6)


# Main area for the scrollable task list
main_list_frame = tk.Frame(content, bg=C("bg"))
main_list_frame.pack(fill="both", expand=True, padx=20, pady=10)

# New container for canvas + scrollbars
scroll_frame = tk.Frame(main_list_frame, bg="#ffd9e8")
scroll_frame.pack(fill="both", expand=True)

# Canvas + scrollbar setup makes the task list scrollable
canvas = tk.Canvas(main_list_frame, bg=C("bg"), highlightthickness=0)
scrollbar = tk.Scrollbar(main_list_frame, orient="vertical", command=canvas.yview)
tasks_frame = tk.Frame(canvas, bg=C("bg"))

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
apply_theme()

# Enable scrolling in the task area
bind_mousewheel(canvas)
bind_mousewheel(tasks_frame)
bind_mousewheel(main_list_frame)

# Start the Tkinter event loop
root.mainloop()