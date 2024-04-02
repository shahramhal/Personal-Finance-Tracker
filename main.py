import tkinter as tk
from gui import setup_gui

# Create tkinter window
root = tk.Tk()
root.title("Personal Finance Tracker")

# Setup GUI
setup_gui(root)

# Run the tkinter event loop
root.mainloop()
