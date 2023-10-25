import tkinter as tk

def save_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(tk.END, f"{len(tasks)}. {task}")
        task_entry.delete(0, tk.END)

def delete_task():
    selection = task_list.curselection()
    if selection:
        index = selection[0]
        task = tasks.pop(index)
        task_list.delete(index)
        status_message.config(text=f"Task '{task}' deleted.")

window = tk.Tk()
window.title("Task Management")
window.geometry("400x400")

task_list = tk.Listbox(window, width=40, height=15)
task_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

task_entry = tk.Entry(window, width=40)
task_entry.pack(padx=10, fill=tk.BOTH, expand=True)

add_button = tk.Button(window, text="Add Task", command=save_task)
delete_button = tk.Button(window, text="Select Task to Delete", command=delete_task)
add_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
delete_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

status_message = tk.Label(window, text="", fg="green")
status_message.pack(pady=10)

tasks = []

window.mainloop()
