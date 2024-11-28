import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
    else:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "No task selected to delete!")

def mark_completed():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"✔ {task}")
    else:
        messagebox.showwarning("Selection Error", "No task selected to mark as completed!")

def save_to_pdf():
    tasks = tasks_listbox.get(0, tk.END)
    if not tasks:
        messagebox.showwarning("Save Error", "No tasks to save!")
        return

    try:
        pdf_file = "todo_list.pdf"
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.drawString(100, 750, "To-Do List")
        c.line(100, 745, 500, 745)

        y = 720
        for task in tasks:
            c.drawString(100, y, f"- {task}")
            y -= 20
            if y < 50:  # Prevent text from going off the page
                c.showPage()
                y = 750

        c.save()
        messagebox.showinfo("Success", f"Tasks saved to {pdf_file}!")
    except Exception as e:
        messagebox.showerror("Save Error", f"An error occurred: {e}")

# Create the main window
app = tk.Tk()
app.title("To-Do List")
app.geometry("500x500")
app.configure(bg="#ffffff")

# Title Label
title_label = tk.Label(app, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#4A90E2")
title_label.place(x=180, y=10)

# Task entry label
task_label = tk.Label(app, text="Enter Your Task:", font=("Helvetica", 12), bg="#f7f7f7", fg="#333333")
task_label.place(x=50, y=60)

# Task entry widget
task_entry = tk.Entry(app, width=30, font=("Helvetica", 12))
task_entry.place(x=170, y=60)

# Buttons in a 2x2 grid
add_button = tk.Button(app, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), relief="flat", width=15)
add_button.place(x=70, y=120)

delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="#F44336", fg="white", font=("Helvetica", 10, "bold"), relief="flat", width=15)
delete_button.place(x=250, y=120)

mark_button = tk.Button(app, text="Mark Completed", command=mark_completed, bg="#FF9800", fg="white", font=("Helvetica", 10, "bold"), relief="flat", width=15)
mark_button.place(x=70, y=170)

save_button = tk.Button(app, text="Save to PDF", command=save_to_pdf, bg="#3F51B5", fg="white", font=("Helvetica", 10, "bold"), relief="flat", width=15)
save_button.place(x=250, y=170)

# Listbox to display tasks with a scrollbar
tasks_frame = tk.Frame(app, bg="#f7f7f7")
tasks_frame.place(x=50, y=220, width=400, height=250)

scrollbar = tk.Scrollbar(tasks_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox = tk.Listbox(tasks_frame, width=40, height=15, font=("Helvetica", 12), yscrollcommand=scrollbar.set, bg="#ffffff", fg="#333333", selectbackground="#D3E4CD")
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=tasks_listbox.yview)

# Run the application
app.mainloop()