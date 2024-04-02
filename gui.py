import tkinter as tk
from tkinter import messagebox
from visualisation import add_income, add_expense

root = tk.Tk()
root.title("Personal Finance Tracker")
# Creating frames 
income_frame = tk.Frame(root)
income_frame.pack(pady=10)

expense_frame = tk.Frame(root)
expense_frame.pack(pady=10)

savings_frame = tk.Frame(root)
savings_frame.pack(pady=10)

#Creating  income widgets 
income_label = tk.Label(income_frame, text="Enter Income Amount:")
income_label.grid(row=0, column=0)

income_entry = tk.Entry(income_frame)
income_entry.grid(row=0, column=1)


#creating expense widgets 
expense_label = tk.Label(expense_frame, text="Enter Expense Amount:")
expense_label.grid(row=0, column=0)

expense_entry = tk.Entry(expense_frame)
expense_entry.grid(row=0, column=1)