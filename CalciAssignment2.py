import tkinter as tk
from tkinter import messagebox
import math

def add_to_expression(symbol):
    current_text = entry_var.get()
    entry_var.set(current_text + str(symbol))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression)
        entry_var.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero")
    except Exception as e:
        messagebox.showerror("Input Error", "Invalid input")

def calculate_function(func):
    try:
        expression = entry_var.get()
        if func == "sqrt":
            result = math.sqrt(eval(expression))
        elif func == "exp":
            result = math.exp(eval(expression))
        elif func == "sin":
            result = math.sin(math.radians(eval(expression)))
        elif func == "cos":
            result = math.cos(math.radians(eval(expression)))
        elif func == "tan":
            result = math.tan(math.radians(eval(expression)))
        elif func == "log":
            result = math.log10(eval(expression))
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Input Error", "Invalid input")

root = tk.Tk()
root.title("Scientific Calculator")

root.geometry("490x600+100+100")
root.configure(bg="#e6e6e6")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0, "blue"), ('8', 1, 1, "#ff6666"), ('9', 1, 2, "#ff6666"), ('/', 1, 3, "#ffcc66"),
    ('4', 2, 0, "green"), ('5', 2, 1, "yellow"), ('6', 2, 2, "#ff6666"), ('*', 2, 3, "#ffcc66"),
    ('1', 3, 0, "#ff6666"), ('2', 3, 1, "#ff6666"), ('3', 3, 2, "#ff6666"), ('-', 3, 3, "#ffcc66"),
    ('0', 4, 0, "white"), ('.', 4, 1, "#ff6666"), ('+', 4, 2, "#ffcc66"), ('=', 4, 3, "#66ccff"),
    ('CE', 5, 0, "#66ff66"), ('sqrt', 5, 2, "#ff66ff"), ('exp', 5, 3, "#ff66ff"),
    ('sin', 6, 0, "#66ffcc"), ('cos', 6, 1, "#66ffcc"), ('tan', 6, 2, "#66ffcc"), ('log', 6, 3, "#66ffcc")
]

for (text, row, col, color) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=30, pady=20, bg=color, command=calculate, font=("Arial", 14))
    elif text == 'CE':
        btn = tk.Button(root, text=text, padx=64, pady=20, bg=color, command=clear_entry, font=("Arial", 14))
        btn.grid(row=row, column=col, columnspan=2)
        continue
    elif text in ['sqrt', 'exp', 'sin', 'cos', 'tan', 'log']:
        btn = tk.Button(root, text=text, padx=30, pady=20, bg=color, command=lambda t=text: calculate_function(t), font=("Arial", 14))
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, bg=color, command=lambda t=text: add_to_expression(t), font=("Arial", 14))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
