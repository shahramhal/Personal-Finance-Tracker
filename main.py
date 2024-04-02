import tkinter as tk
import json
import os 


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

#Create Tkinter 
root = tk.Tk()
root.title("Personal Finance Tracker")