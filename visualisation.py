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
    """Visualize financial data as a pie chart."""
    data = load_data()
    income_total = sum(sum(income) for income in data["income"].values())
    expenses_total = sum(sum(expenses) for expenses in data["expenses"].values())

    # Pie chart
    labels = ['Income', 'Expenses']
    sizes = [income_total, expenses_total]
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # explode 1st slice

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Income vs Expenses')
    plt.show()
def display_summary():
    """Display a summary of income, expenses, and savings goals."""
    data = load_data()
    income_total = sum(sum(income) for income in data["income"].values())
    expenses_total = sum(sum(expenses) for expenses in data["expenses"].values())
    savings_goals = data["savings_goals"]

    summary = f"Total Income: ${income_total}\n"
    summary += f"Total Expenses: ${expenses_total}\n"
    summary += "Savings Goals:\n"
    for goal, amount in savings_goals.items():
        summary += f"- {goal}: ${amount}\n"
    
    messagebox.showinfo("Summary", summary)