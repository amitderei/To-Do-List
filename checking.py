import tkinter as tk
from tkinter import ttk
def show_selected_choice():
    selected_option = var.get()
    print(f"Selected option: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Multiple Choice Example")

# Variable to hold the selected option
var = tk.StringVar(value="Option 1")  # Default value

# Create radio buttons
options = ["Option 1", "Option 2", "Option 3"]
for option in options:
    rb = tk.Radiobutton(root, text=option, variable=var, value=option, command=show_selected_choice)
    rb.pack(anchor=tk.W)

# Button to submit choice
submit_button = ttk.Button(root, text="Submit", command=show_selected_choice)
submit_button.pack()

root.mainloop()