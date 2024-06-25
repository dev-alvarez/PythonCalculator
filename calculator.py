import tkinter as tk
from numpy import sin, cos, tan, log, sqrt, pi, e

safe_dict = {"sin": sin, "cos": cos, "tan": tan, "log": log, "sqrt": sqrt, "pi": pi, "e": e}

def evaluate(event=None):
    expr = entry.get()
    try:
        result = str(eval(expr, {"__builtins__": None}, safe_dict))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(value):
    if value == "=":
        evaluate()
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=5)
entry.bind("<Return>", evaluate) 

buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'log',
    'sqrt', '(', ')', 'pi', 'e'
]

row, col = 1, 0
for button in buttons:
    action = lambda x=button: button_click(x)
    tk.Button(root, text=button, width=5, command=action).grid(row=row, column=col) 
    col += 1
    if col > 4:
        col = 0
        row += 1
tk.Button(root, text='C', width=5, command=lambda: entry.delete(0, tk.END)).grid(row=row, column=col)
root.mainloop()
