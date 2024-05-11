import tkinter as tk

# Function to handle button clicks
def button_click(event):
    # Get the text of the clicked button
    text = event.widget.cget("text")

    # Handle different button clicks
    if text == "=":
        try:
            # Evaluate the expression and update the display
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        # Clear the display
        entry.delete(0, tk.END)
    else:
        # Append the clicked button's text to the display
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and configure the entry widget for display
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons' text
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Create and place the buttons
row_num = 1
col_num = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20)
    button.grid(row=row_num, column=col_num, padx=5, pady=5)

    # Bind button click event to button_click function
    button.bind("<Button-1>", button_click)

    # Update row and column numbers
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Run the main event loop
root.mainloop()

