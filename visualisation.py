import json
import os
import matplotlib.pyplot as plt
from tkinter import messagebox


financial_data_file = "financial_data.json"

def initialize():
    """Initialize the program."""
    if not os.path.exists(financial_data_file):
        with open(financial_data_file, 'w') as f:
            json.dump({
                "income": {"Salary": [], "Investment": []},
                "expenses": {"House": [], "Groceries": [],
                             "Entertainment": [], "Transport": [], 
                             "Shopping": [], "services": [], "other": []},
                "savings_goals": {}
            }, f)

def load_data():
    """Load financial data from file."""
    if os.path.exists(financial_data_file):
        with open(financial_data_file, 'r') as f:
            return json.load(f)
    else:
        initialize()
        return load_data()

def save_data(data):
    """Save financial data to file."""
    with open(financial_data_file, 'w') as f:
        json.dump(data, f)

def add_income(category, amount):
    """Add income to the financial data."""
    data = load_data()
    if category not in data["income"]:
        data["income"][category] = []
    data["income"][category].append(amount)
    save_data(data)


def add_expense(category, amount):
    """Add expense to the financial data."""
    data = load_data()
    if category not in data["expenses"]:
        data["expenses"][category] = []
    data["expenses"][category].append(amount)
    save_data(data)

def add_savings_goal(goal, amount):
    """Add a savings goal to the financial data."""
    data = load_data()
    data["savings_goals"][goal] = amount
    save_data(data)
    
def visualize_data():
    """Visualize financial data as pie charts for income and expenses by categories."""
    data = load_data()
    income_data = data["income"]
    expense_data = data["expenses"]

    # Pie chart for Income by Category
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.pie([sum(amounts) for amounts in income_data.values()], labels=income_data.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Income by Category (£)')

    # Pie chart for Expenses by Category
    plt.subplot(1, 2, 2)
    plt.pie([sum(amounts) for amounts in expense_data.values()], labels=expense_data.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category (£)')

    plt.tight_layout()
    plt.show()
def display_summary():
    """Display a summary of income, expenses, savings goals, and balance."""
    data = load_data()
    income_summary = "Income by Category:\n"
    total_income = 0
    for category, amounts in data["income"].items():
        total_amount = sum(amounts)
        total_income += total_amount
        income_summary += f"- {category}: £{total_amount}\n"
    
    expense_summary = "\nExpenses by Category:\n"
    total_expenses = 0
    for category, amounts in data["expenses"].items():
        total_amount = sum(amounts)
        total_expenses += total_amount
        expense_summary += f"- {category}: £{total_amount}\n"
    
    savings_goals = "\nSavings Goals:\n"
    total_savings = 0
    remaining_savings = {}
    for goal, amount in data["savings_goals"].items():
        total_savings += amount
        saved_amount = sum(data["expenses"].get(goal, []))
        remaining_amount = max(0, amount - saved_amount)
        remaining_savings[goal] = remaining_amount
        savings_goals += f"- {goal}: £{remaining_amount} remaining out of £{amount}\n"
    
    total_summary = f"\nTotal Income: £{total_income}\nTotal Expenses: £{total_expenses}\nTotal Savings Goals: £{total_savings}\n"
    
    balance = total_income - total_expenses
    balance_summary = f"\nBalance: £{balance}\n"

    summary = income_summary + expense_summary + savings_goals + total_summary + balance_summary
    messagebox.showinfo("Summary", summary)
