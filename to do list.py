# TO-DO LIST

from tkinter import *
from tkinter import messagebox
import os

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
 
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "No task selected!")

def mark_task_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        if not task.startswith("[Completed]"):
            task_listbox.delete(selected_task)
            task_listbox.insert(END, f"[Completed] {task}")
        else:
            messagebox.showinfo("Info", "Task is already marked as completed!")
    else:
        messagebox.showwarning("Warning", "No task selected!")

def clear_all_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, END)

def clear_completed_tasks():
    tasks = task_listbox.get(0, END)
    task_listbox.delete(0, END)
    for task in tasks:
        if not task.startswith("[Completed]"):
            task_listbox.insert(END, task)

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(END, task.strip())

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Main Window
root = Tk()
root.title("To-Do List Application")
root.attributes('-fullscreen', True)  # Start in full-screen mode
root.bind('<Escape>', exit_fullscreen)
root.config(bg="LightBlue")

# Title Label
title_label = Label(root, text="To-Do List", font=("Helvetica", 20, "bold"), bg="LightBlue", fg="Black")
title_label.pack(pady=10)

# Task Input Frame
task_frame = Frame(root, bg="LightBlue")
task_frame.pack(pady=10)

task_entry = Entry(task_frame, font=("Helvetica", 14), width=30)
task_entry.grid(row=0, column=0, padx=5)

add_task_btn = Button(task_frame, text="Add Task", font=("Helvetica", 12), bg="Green", fg="White", width=10, command=add_task)
add_task_btn.grid(row=0, column=1, padx=5)

# Task Listbox with Scrollbar
listbox_frame = Frame(root, bg="LightBlue")
listbox_frame.pack(pady=10)

task_listbox = Listbox(listbox_frame, width=50, height=15, font=("Helvetica", 12), selectbackground="Gray", activestyle="none")
task_listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Button Frame
button_frame = Frame(root, bg="LightBlue")
button_frame.pack(pady=10)

delete_task_btn = Button(button_frame, text="Delete Task", font=("Helvetica", 12), bg="Red", fg="White", width=12, command=delete_task)
delete_task_btn.grid(row=0, column=0, padx=5, pady=5)

mark_completed_btn = Button(button_frame, text="Mark Completed", font=("Helvetica", 12), bg="Orange", fg="White", width=12, command=mark_task_completed)
mark_completed_btn.grid(row=0, column=1, padx=5, pady=5)

clear_all_btn = Button(button_frame, text="Clear All", font=("Helvetica", 12), bg="DarkRed", fg="White", width=12, command=clear_all_tasks)
clear_all_btn.grid(row=1, column=0, padx=5, pady=5)

clear_completed_btn = Button(button_frame, text="Clear Completed", font=("Helvetica", 12), bg="Purple", fg="White", width=12, command=clear_completed_tasks)
clear_completed_btn.grid(row=1, column=1, padx=5, pady=5)

save_tasks_btn = Button(button_frame, text="Save Tasks", font=("Helvetica", 12), bg="Blue", fg="White", width=12, command=save_tasks)
save_tasks_btn.grid(row=2, column=0, padx=5, pady=5)

load_tasks_btn = Button(button_frame, text="Load Tasks", font=("Helvetica", 12), bg="Teal", fg="White", width=12, command=load_tasks)
load_tasks_btn.grid(row=2, column=1, padx=5, pady=5)

# Load tasks on startup
load_tasks()

# Run the Application
root.mainloop()
