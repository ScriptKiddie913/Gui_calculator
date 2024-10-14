import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

# Function to handle button clicks
def button_click(value):
    current_expression = entry.get()
    new_expression = current_expression + str(value)
    entry.delete(0, tk.END)
    entry.insert(0, new_expression)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    current_expression = entry.get()
    result = evaluate_expression(current_expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying the expression
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=clear_entry)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Run the main loop
root.mainloop()

