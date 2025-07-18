import tkinter as tk
from tkinter import messagebox
import numpy as np

# Function to process input and perform operations
def process_array(operation):
    try:
        # Get user input and convert to NumPy array
        user_input = entry.get()
        numbers = list(map(float, user_input.split(',')))
        arr = np.array(numbers)

        # Perform the selected operation
        if operation == 'multiply':
            result = arr * 2
        elif operation == 'square':
            result = arr ** 2
        elif operation == 'mean':
            result = np.mean(arr)
        elif operation == 'sum':
            result = np.sum(arr)
        else:
            result = "Invalid operation"

        output_label.config(text=f"Result: {result}")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Setup GUI window
root = tk.Tk()
root.title("NumPy GUI Example")
root.geometry("400x300")

# Entry for user input
tk.Label(root, text="Enter comma-separated numbers:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack()

# Buttons for different operations
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="×2", command=lambda: process_array('multiply')).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Square", command=lambda: process_array('square')).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Mean", command=lambda: process_array('mean')).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Sum", command=lambda: process_array('sum')).grid(row=0, column=3, padx=5)

# Label to show result
output_label = tk.Label(root, text="Result: ", font=("Arial", 12))
output_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
