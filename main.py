import tkinter as tk  # Import the tkinter module for GUI development

# Function to handle button clicks
def click(event):
    current = str(entry.get())              # Get the current text from the entry field
    text = event.widget.cget("text")        # Get the text of the button clicked

    if text == "=":                         # If '=' button is clicked
        try:
            result = eval(current)          # Evaluate the expression using eval()
            entry.delete(0, tk.END)         # Clear the entry field
            entry.insert(tk.END, str(result))  # Insert the result into the entry field
        except Exception as e:              # Handle any errors (like division by zero)
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")   # Display 'Error' if evaluation fails

    elif text == "C":                       # If 'C' button is clicked
        entry.delete(0, tk.END)             # Clear the entry field

    else:
        entry.insert(tk.END, text)          # Append the button text to the entry field

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")             # Set window title
root.geometry("300x400")                    # Set window size
root.resizable(False, False)               # Disable resizing of the window

# Entry widget to display user input and results
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)  # Pack entry widget with padding

# Frame to hold the calculator buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

# 2D list of button labels
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Loop through each row in the button layout
for row in buttons:
    r = tk.Frame(btn_frame)     # Create a new frame for each row
    r.pack(expand=True, fill="both")  # Expand to fill available space
    for char in row:
        b = tk.Button(r, text=char, font="Arial 18", height=2, width=4)  # Create button
        b.pack(side="left", expand=True, fill="both")                    # Pack button
        b.bind("<Button-1>", click)  # Bind left-click event to the click() function

# Start the Tkinter event loop
root.mainloop()
