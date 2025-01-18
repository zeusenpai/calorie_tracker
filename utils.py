import matplotlib.pyplot as plt
from data_manager import *
from tabulate import tabulate
from datetime import date
import json
import os

# Paths to data
users_path = "data/users.json"
logs_path = "data/"

def generate_daily_report(user_name):
    # Load user data
    with open(users_path, "r") as file:
        users = json.load(file)

    user = next((u for u in users if u["name"] == user_name), None)
    if not user:
        print(f"User '{user_name}' not found.")
        return

    # Load logs
    log_file = os.path.join(logs_path, f"{user_name}_logs.json")
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            logs = json.load(file)
    else:
        print("No logs found for today.")
        return

    today = str(date.today())
    daily_log = logs.get(today, {"calories_consumed": 0, "food_items": [], "calories_burned": 0})

    calories_consumed = daily_log.get("calories_consumed", 0)
    calories_burned = daily_log.get("calories_burned", 0)

    # Calculate calorie balance
    tdee = user["tdee"]
    calorie_balance = tdee - (calories_consumed - calories_burned)

    # Macronutrient goals
    target_calories = tdee
    macronutrient_ratios = {"Carbs": 0.5, "Protein": 0.3, "Fat": 0.2}
    macronutrients = {
        macro: round((target_calories * ratio) / (4 if macro in ["Carbs", "Protein"] else 9), 2)
        for macro, ratio in macronutrient_ratios.items()
    }

    # Generate Report
    report_data = [
        ["Calories Consumed", f"{calories_consumed} kcal"],
        ["Calories Burned", f"{calories_burned} kcal"],
        ["Calorie Balance", f"{calorie_balance} kcal"],
        ["TDEE (Goal)", f"{tdee} kcal"],
        ["Macronutrient Goals", ""],
    ]
    for macro, grams in macronutrients.items():
        report_data.append([f"  {macro}", f"{grams} g"])

    print("\nDaily Report")
    print(tabulate(report_data, headers=["Metric", "Value"], tablefmt="pretty"))