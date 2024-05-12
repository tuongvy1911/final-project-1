import tkinter as tk
import math

def button_click(symbol):
    current = display_var.get()
    if symbol == 'C':
        display_var.set('')
    elif symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set('Error')
    else:
        display_var.set(current + symbol)

def trig_function(func):
    current = display_var.get()
    try:
        if func == 'sin':
            result = math.sin(math.radians(float(current)))
        elif func == 'cos':
            result = math.cos(math.radians(float(current)))
        elif func == 'csc':
            result = 1 / math.sin(math.radians(float(current)))
        elif func == 'sec':
            result = 1 / math.cos(math.radians(float(current)))
        display_var.set(str(result))
    except:
        display_var.set('Error')

def square_root():
    current = display_var.get()
    try:
        result = math.sqrt(float(current))
        display_var.set(str(result))
    except:
        display_var.set('Error')

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the input
display_var = tk.StringVar()

# Create the display
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, insertwidth=4, width=18, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('csc', 5, 2), ('sec', 5, 3),
    ('sqrt', 6, 0), ('=', 6, 1)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text in ['sin', 'cos', 'csc', 'sec']:
        btn = tk.Button(root, text=text, font=('Arial', 12), padx=20, pady=20, command=lambda t=text: trig_function(t))
    elif text == 'sqrt':
        btn = tk.Button(root, text=text, font=('Arial', 12), padx=20, pady=20, command=square_root)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 12), padx=20, pady=20, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

root.mainloop()
