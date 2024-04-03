import tkinter as tk
from tkinter import messagebox
from visualisation import add_income, add_expense


def setup_gui(root):
    def handle_add_income():
        try:
            amount = float(income_entry.get())
            add_income(amount)
            messagebox.showinfo("Success", "Income added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for income amount.")

    def handle_add_expense():
        try:
            amount = float(expense_entry.get())
            add_expense(amount)
            messagebox.showinfo("Success", "Expense added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for expense amount.")

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