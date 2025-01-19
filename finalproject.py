import json
import os
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from tabulate import tabulate

# Paths to data
users_path = "data/users.json"
logs_path = "data/"

class User:
    def __init__(self, name, age, gender, height, weight, activity_level, goal):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal = goal
        self.bmr = self.calculate_bmr()
        self.tdee = self.calculate_tdee()

    def calculate_bmr(self):
        if self.gender.lower() == "m":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender.lower() == "f":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        else:
            raise ValueError("Invalid gender")
        return bmr

    def calculate_tdee(self):
        activity_multipliers = {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9
        }

        multiplier = activity_multipliers.get(self.activity_level, 1.2)
        tdee = self.bmr * multiplier

        if self.goal == 1:
            tdee -= 500
        elif self.goal == 2:
            tdee += 250

        return round(tdee)

class Log:
    def __init__(self, name):
        self.name = name
        self.date = str(date.today())
        self.calories_consumed = 0
        self.food_items = []

    def add_food(self, food, calories):
        self.food_items.append({"food": food, "calories": calories})
        self.calories_consumed += calories
        save_logs(self.name, self.food_items, self.calories_consumed)
        print(f"Added '{food}' with {calories} kcal.")

# Data Manager Functions
def save_user(user):
    if os.path.exists(users_path):
        try:
            with open(users_path, "r") as file:
                users = json.load(file)
        except (json.JSONDecodeError, IOError):
            users = []
    else:
        users = []

    user_exists = False
    for existing_user in users:
        if existing_user["name"] == user.name:
            existing_user.update({
                "age": user.age,
                "gender": user.gender,
                "height": user.height,
                "weight": user.weight,
                "activity_level": user.activity_level,
                "goal": user.goal,
                "bmr": user.bmr,
                "tdee": user.tdee
            })
            print("User details updated!")
            user_exists = True
            break

    if not user_exists:
        users.append({
            "name": user.name,
            "age": user.age,
            "gender": user.gender,
            "height": user.height,
            "weight": user.weight,
            "activity_level": user.activity_level,
            "goal": user.goal,
            "bmr": user.bmr,
            "tdee": user.tdee
        })

    try:
        with open(users_path, "w") as file:
            json.dump(users, file, indent=4)
        print(f"User '{user.name}' saved successfully.")
    except IOError as e:
        print(f"Error saving user: {e}")

def load_users():
    if os.path.exists(users_path):
        try:
            with open(users_path, "r") as file:
                users = json.load(file)
        except (json.JSONDecodeError, IOError):
            users = []
    else:
        users = []

    df = pd.DataFrame(users)
    print(df)

def save_logs(name, food_items, calories_consumed):
    log_path = os.path.join(logs_path, f"{name}_logs.json")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    if os.path.exists(log_path):
        try:
            with open(log_path, "r") as file:
                logs = json.load(file)
        except (json.JSONDecodeError, IOError):
            logs = {}
    else:
        logs = {}

    logs[str(date.today())] = {
        "calories_consumed": calories_consumed,
        "food_items": food_items
    }

    try:
        with open(log_path, "w") as file:
            json.dump(logs, file, indent=4)
        print("Log saved successfully.")
    except IOError as e:
        print(f"Error saving log: {e}")

def generate_daily_report(user_name):
    with open(users_path, "r") as file:
        users = json.load(file)

    user = next((u for u in users if u["name"] == user_name), None)
    if not user:
        print(f"User '{user_name}' not found.")
        return

    log_file = os.path.join(logs_path, f"{user_name}_logs.json")
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            logs = json.load(file)
    else:
        print("No logs found for today.")
        return

    today = str(date.today())
    daily_log = logs.get(today, {"calories_consumed": 0, "food_items": []})

    calories_consumed = daily_log.get("calories_consumed", 0)
    tdee = user["tdee"]
    calorie_balance = tdee - calories_consumed

    print("\nDaily Report")
    print(tabulate([
        ["Calories Consumed", f"{calories_consumed} kcal"],
        ["Calorie Balance", f"{calorie_balance} kcal"],
        ["TDEE (Goal)", f"{tdee} kcal"]
    ], headers=["Metric", "Value"], tablefmt="pretty"))

# Menu-driven Program
def main_menu():
    while True:
        print("============================================")
        print("            CALORIE TRACKER")
        print("============================================")
        print("Main Menu:")
        print("1. Add a new user")
        print("2. View all users")
        print("3. Log food")
        print("4. Generate daily report")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender (M/F): ").lower()
            height = float(input("Height (cm): "))
            weight = float(input("Weight (kg): "))
            print("Activity Level: \n1.Not Active\n2.Lightly Active\n3.Moderately Active\n4.Very Active\n5.Extremely Active")
            activity_level = int(input("Activity Level (1-5): "))
            goal = int(input("Goal (1: Lose Weight, 2: Gain Weight, 3: Maintain Weight): "))
            user = User(name, age, gender, height, weight, activity_level, goal)
            save_user(user)
        elif choice == "2":
            load_users()
        elif choice == "3":
            name = input("Enter user name: ")
            while 1:
            
                food = input("Enter food name: ")
                calories = int(input("Enter calories: "))
                log = Log(name)
                log.add_food(food, calories)
                ch=input("Do you want to continue?y/n:")
                if ch.lower()== 'n':
                    break
                else:
                    continue
            
        elif choice == "4":
            name = input("Enter user name: ")
            generate_daily_report(name)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main_menu()
