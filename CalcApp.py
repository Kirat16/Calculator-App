import tkinter as tk
import math

# Initialize window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x600")
root.resizable(False, False)

expression = ""

# Display field
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=25, pady=20)

# Function to update entry
def press(symbol):
    global expression
    expression += str(symbol)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Scientific functions
def sci_func(func):
    global expression
    try:
        value = float(eval(expression))
        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Button definitions
buttons = [
    ("C", clear), ("(", lambda: press("(")), (")", lambda: press(")")), ("/", lambda: press("/")), ("sqrt", lambda: sci_func("sqrt")),
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("*", lambda: press("*")), ("log", lambda: sci_func("log")),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-")), ("ln", lambda: sci_func("ln")),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+")), ("^", lambda: press("**")),
    ("0", lambda: press("0")), (".", lambda: press(".")), ("=", equal), ("sin", lambda: sci_func("sin")), ("cos", lambda: sci_func("cos")),
    ("tan", lambda: sci_func("tan"))
]

# Add buttons to grid
row = 1
col = 0
for (text, command) in buttons:
    tk.Button(root, text=text, width=6, height=2, font=("Arial", 14),
              command=command, bg="#f0f0f0").grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()
