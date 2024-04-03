import json
import os
import matplotlib.pyplot as plt

financial_data_file = "financial_data.json"

def initialize():
    """Initialize the program."""
    if not os.path.exists(financial_data_file):
        with open(financial_data_file, 'w') as f:
            json.dump({"income": [], "expenses": [], "savings_goals": {}}, f)

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

def add_income(amount):
    """Add income to the financial data."""
    data = load_data()
    data["income"].append(amount)
    save_data(data)


def add_expense(amount):
    """Add expense to the financial data."""
    data = load_data()
    data["expenses"].append(amount)
    save_data(data)

def add_savings_goal(goal, amount):
    """Add a savings goal to the financial data."""
    data = load_data()
    data["savings_goals"][goal] = amount
    save_data(data)
    
def visualize_data():
    """Visualize financial data."""
    data = load_data()
    income = data["income"]
    expenses = data["expenses"]
    
    # Generate x values (assuming equal intervals for simplicity)
    x_values = list(range(1, len(income) + 1))

    # Plot income and expenses
    plt.plot(x_values, income, label='Income', marker='o')
    plt.plot(x_values, expenses, label='Expenses', marker='o')

    # Add labels and title
    plt.xlabel('Days')
    plt.ylabel('Amount ($)')
    plt.title('Income vs Expenses')

    # Add legend
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.show()
