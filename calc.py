import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(symbol):
    entry.insert(tk.END, symbol)

def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget for displaying and entering numbers
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('%', 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 16), padx=20, pady=10,
                       command=lambda symbol=button_text: button_click(symbol))
    button.grid(row=row, column=column, padx=5, pady=5)

# Create a button to clear the entry
clear_button = tk.Button(root, text="C", font=('Arial', 16), padx=20, pady=10, command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create a button to calculate the result
calc_button = tk.Button(root, text="=", font=('Arial', 16), padx=20, pady=10, command=calculate)
calc_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
