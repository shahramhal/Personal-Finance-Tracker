import tkinter as tk
import json
import os 



financial_data_file = "financial_data.json"

def initialize():
    """Initialize the program."""
    if not os.path.exists(financial_data_file):
        with open(financial_data_file, 'w') as f:
            json.dump({"income": [], "expenses": [], "savings_goals": {}}, f)
