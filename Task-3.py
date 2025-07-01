import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_symbols, use_numbers):
    if length < 1:
        return "Password length must be at least 1."

    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits if use_numbers else ''
    special_characters = string.punctuation if use_symbols else ''

    
    all_characters = lowercase + uppercase + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        use_symbols = var_symbols.get()
        use_numbers = var_numbers.get()
        
        if length < 1:
            messagebox.showerror("Error", "Please enter a positive integer.")
        else:
            generated_password = generate_password(length, use_symbols, use_numbers)
            label_result.config(text=f"Generated Password: {generated_password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  
root.configure(bg='lightblue')  

 
label_length = tk.Label(root, text="Enter the desired length of the password:", bg='lightblue')
label_length.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

var_symbols = tk.BooleanVar()
check_symbols = tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, bg='lightblue')
check_symbols.pack(pady=5)

var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg='lightblue')
check_numbers.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Helvetica", 12), bg='lightblue')
label_result.pack(pady=10)


root.mainloop()
