import tkinter as tk
from tkinter import messagebox
from visualisation import add_income, add_expense, add_savings_goal, display_summary, visualize_data, delete_last_income, delete_last_expense, delete_last_savings_goal

# Define categories for income and expenses
income_categories = ["Salary", "Investment", "Other"]
expense_categories = ["House", "Groceries", "Entertainment", "Transport", "Shopping", "Services", "Other"]


def setup_gui(root):
    # Error Handling part
    def error_add_income(): #Error Handling for income 
        try:
            category = income_category_var.get()
            amount = float(income_entry.get())
            add_income(category, amount)
            messagebox.showinfo("Success", "Income added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for income amount.")

    def error_add_expense():#Error Handling for expense button 
        try:
            category = expense_category_var.get()
            amount = float(expense_entry.get())
            add_expense(category, amount)
            messagebox.showinfo("Success", "Expense added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for expense amount.")

    def error_add_savings_goal():#Error Handling for saving goal button 
        goal = savings_goal_entry.get()
        try:
            amount = float(savings_amount_entry.get())
            add_savings_goal(goal, amount)
            messagebox.showinfo("Success", "Savings goal added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for savings amount.")

    def error_visualize_data():#Error Handling for income 
        try:
            visualize_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def error_display_summary():#Error Handling for summary display button  
        try:
            display_summary()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Creating frames
    root.title("Personal Finance Tracker")

    income_frame = tk.Frame(root)
    income_frame.pack(pady=10)

    expense_frame = tk.Frame(root)
    expense_frame.pack(pady=10)

    savings_frame = tk.Frame(root)
    savings_frame.pack(pady=10)

    summary_frame = tk.Frame(root)
    summary_frame.pack(pady=10)

    # Creating income widgets
    income_label = tk.Label(income_frame, text="Enter Income Amount:")
    income_label.grid(row=0, column=0)

    income_entry = tk.Entry(income_frame)
    income_entry.grid(row=0, column=1)

    income_category_label = tk.Label(income_frame, text="Select Category:")
    income_category_label.grid(row=1, column=0)

    income_category_var = tk.StringVar()
    income_category_var.set(income_categories[0])
    income_category_menu = tk.OptionMenu(income_frame, income_category_var, *income_categories)
    income_category_menu.grid(row=1, column=1)

    income_button = tk.Button(income_frame, text="Add Income", command=error_add_income)
    income_button.grid(row=2, columnspan=2, pady=5)

    # Delete Last Income Button
    delete_income_button = tk.Button(income_frame, text="Delete last action", command= delete_last_income)
    delete_income_button.grid(row=3, columnspan=2, pady=5)

    # Creating expense widgets
    expense_label = tk.Label(expense_frame, text="Enter Expense Amount:")
    expense_label.grid(row=0, column=0)

    expense_entry = tk.Entry(expense_frame)
    expense_entry.grid(row=0, column=1)

    expense_category_label = tk.Label(expense_frame, text="Select Category:")
    expense_category_label.grid(row=1, column=0)

    expense_category_var = tk.StringVar()
    expense_category_var.set(expense_categories[0])
    expense_category_menu = tk.OptionMenu(expense_frame, expense_category_var, *expense_categories)
    expense_category_menu.grid(row=1, column=1)

    expense_button = tk.Button(expense_frame, text="Add Expense", command=error_add_expense)
    expense_button.grid(row=2, columnspan=2, pady=5)

    # Delete Last Expense Button
    delete_expense_button = tk.Button(expense_frame, text="Delete last action", command= delete_last_expense)
    delete_expense_button.grid(row=3, columnspan=2, pady=5)

    # Display Summary Button
    summary_button = tk.Button(summary_frame, text="Display Summary", command=error_display_summary)
    summary_button.pack()

    # Creating Savings Goal widgets
    savings_goal_label = tk.Label(savings_frame, text="Enter Savings Goal:")
    savings_goal_label.grid(row=0, column=0)

    savings_goal_entry = tk.Entry(savings_frame)
    savings_goal_entry.grid(row=0, column=1)

    savings_amount_label = tk.Label(savings_frame, text="Enter Amount:")
    savings_amount_label.grid(row=1, column=0)

    savings_amount_entry = tk.Entry(savings_frame)
    savings_amount_entry.grid(row=1, column=1)

    savings_button = tk.Button(savings_frame, text="Add Savings Goal", command=error_add_savings_goal)
    savings_button.grid(row=2, column=1)

    # Delete Last Savings Goal Button
    delete_savings_button = tk.Button(savings_frame, text="Delete last action", command=delete_last_savings_goal)
    delete_savings_button.grid(row=3, columnspan=2, pady=5)

    # Visualize Data Button
    visualize_button = tk.Button(summary_frame, text="Visualize Data", command=error_visualize_data)
    visualize_button.pack()

    root.mainloop()
