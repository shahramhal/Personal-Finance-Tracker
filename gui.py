import tkinter as tk
from tkinter import messagebox
from visualisation import add_income, add_expense, add_savings_goal, display_summary


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
    def handle_add_savings_goal():
        goal = savings_goal_entry.get()
        try:
            amount = float(savings_amount_entry.get())
            add_savings_goal(goal, amount)
            messagebox.showinfo("Success", "Savings goal added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for savings amount.")

    # Creating frames 
    income_frame = tk.Frame(root)
    income_frame.pack(pady=10)

    expense_frame = tk.Frame(root)
    expense_frame.pack(pady=10)

    savings_frame = tk.Frame(root)
    savings_frame.pack(pady=10)

    summary_frame = tk.Frame(root)
    summary_frame.pack(pady=10)

    #Creating  income widgets 
    income_label = tk.Label(income_frame, text="Enter Income Amount:")
    income_label.grid(row=0, column=0)

    income_entry = tk.Entry(income_frame)
    income_entry.grid(row=0, column=1)


    income_button = tk.Button(income_frame, text="Add Income", command=handle_add_income)
    income_button.grid(row=0, column=2)



    #creating expense widgets 
    expense_label = tk.Label(expense_frame, text="Enter Expense Amount:")
    expense_label.grid(row=0, column=0)

    expense_entry = tk.Entry(expense_frame)
    expense_entry.grid(row=0, column=1)

    expense_button = tk.Button(expense_frame, text="Add Expense", command=handle_add_expense)
    expense_button.grid(row=0, column=2)

    # Creating Savings Goal widgets
    savings_goal_label = tk.Label(savings_frame, text="Enter Savings Goal:")
    savings_goal_label.grid(row=0, column=0)

    savings_goal_entry = tk.Entry(savings_frame)
    savings_goal_entry.grid(row=0, column=1)

    savings_amount_label = tk.Label(savings_frame, text="Enter Amount:")
    savings_amount_label.grid(row=1, column=0)

    savings_amount_entry = tk.Entry(savings_frame)
    savings_amount_entry.grid(row=1, column=1)

    savings_button = tk.Button(savings_frame, text="Add Savings Goal", command=handle_add_savings_goal)
    savings_button.grid(row=2, column=1)
    # Creating Summary widgets 
    summary_button = tk.Button(summary_frame, text="Display Summary", command=display_summary)
    summary_button.grid(row=0, column=0, padx=10)

