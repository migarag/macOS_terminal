import tkinter as tk

# Function to update expression in the text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Main code for the calculator GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")

    expression = ""
    equation = tk.StringVar()

    # Create the text entry box for showing the expression
    expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
    expression_field.grid(columnspan=4)

    # Create buttons for the calculator
    buttons = [
        '7', '8', '9', '/', 
        '4', '5', '6', '*', 
        '1', '2', '3', '-', 
        '0', '.', '=', '+'
    ]

    row = 1
    col = 0
    for button in buttons:
        if button == "=":
            tk.Button(root, text=button, font=('Arial', 20), command=equalpress, height=2, width=7).grid(row=row, column=col, columnspan=2)
            col += 1
        else:
            tk.Button(root, text=button, font=('Arial', 20), command=lambda b=button: press(b), height=2, width=7).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Add a clear button
    tk.Button(root, text='C', font=('Arial', 20), command=clear, height=2, width=7).grid(row=row, column=col)

    # Run the GUI
    root.mainloop()
