import tkinter as tk 
from numpy import sin, cos, tan, log, sqrt, pi, e 

def evaluate(event=None):
    expr = entry.get()
    try:
        result = str(eval(expr, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan:" tan, "log": log, "sqrt": sqrt, "pi": pi, "e": e}))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Scientific Calculator")
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
    action = lambda x=button: entry.insert(tk.END, x)
    tk.Button(root, text=button, ) u
