import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.configure(bg="#efae6d")
        
        self.tasks = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Task entry
        self.task_entry = tk.Entry(main_frame, font=('Arial', 12), width=30,
                                 bg='white', fg='black')
        self.task_entry.pack(pady=10)
        
        # Add button
        add_btn = tk.Button(main_frame, text="Add Task", command=self.add_task,
                          bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
        add_btn.pack(pady=5)
        
        # Task list with numbers
        self.task_listbox = tk.Listbox(main_frame, font=('Arial', 12), 
                                     height=15, width=45, selectmode=tk.SINGLE,
                                     bg='white', fg='black', selectbackground='#4CAF50')
        self.task_listbox.pack(pady=10)
        
        # Remove button
        remove_btn = tk.Button(main_frame, text="Remove Selected", 
                             command=self.remove_task,
                             bg='#f44336', fg='white', font=('Arial', 10, 'bold'))
        remove_btn.pack(pady=5)
        
        # Bind Enter key
        self.root.bind('<Return>', lambda event: self.add_task())
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Cannot add an empty task")
    
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        # Add numbered tasks
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
