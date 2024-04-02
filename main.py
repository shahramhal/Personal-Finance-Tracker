import tkinter as tk
import json
import os 
import matplotlib as plt 


#Json file 
financial_data_file = "financial_data.json"
#initializing the programm 
def initialize():

    if not os.path.exists(financial_data_file):
        with open(financial_data_file, 'w') as f:
            json.dump({"income": [], "expenses": [], "savings_goals": {}}, f)
#Load data 
def load_data():

    if os.path.exists(financial_data_file):
        with open(financial_data_file, 'r') as f:
            return json.load(f)
    else:
        initialize()
        return load_data()

#Save data 
def save_data(data):

    with open(financial_data_file, 'w') as f:
        json.dump(data, f)

#Creating Graph 
def visualize_data():
    data = load_data()
    income = data["income"]
    expenses = data["expenses"]
    
    # Generate x values (assuming equal intervals for simplicity)
    x_values = list(range(1, len(income) + 1))

    # Plot income and expenses
    plt.plot(x_values, income, label='Income', marker='o')
    plt.plot(x_values, expenses, label='Expenses', marker='o')

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.title('Income vs Expenses')

    # Add legend
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.show()

#Create Tkinter 
root = tk.Tk()
root.title("Personal Finance Tracker")
root.mainloop()