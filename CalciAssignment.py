import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = var.get()

        if operation == "Divide":
            result = num1 / num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero")


root = tk.Tk()
root.title("Calculator with Operations")


root.geometry("300x300+100+100")


entry1 = tk.Entry(root)
entry1.pack(pady=5) 
entry2 = tk.Entry(root)
entry2.pack(pady=5) 

var = tk.StringVar()
var.set("Add")  
radio1 = tk.Radiobutton(root, text="Add", variable=var, value="Add")
radio2 = tk.Radiobutton(root, text="Subtract", variable=var, value="Subtract")
radio3 = tk.Radiobutton(root, text="Multiply", variable=var, value="Multiply")
radio4 = tk.Radiobutton(root, text="Divide", variable=var, value="Divide")

radio1.pack(anchor=tk.W)
radio2.pack(anchor=tk.W)
radio3.pack(anchor=tk.W)
radio4.pack(anchor=tk.W)


calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)  


result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5) 
root.mainloop()
