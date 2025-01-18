import json
import os
import pandas as pd

users_path = "data/users.json"

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
            print("user details updated!")
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
    
    return users
    """df = pd.DataFrame(users)
    print(df)"""

def save_logs(self, name, food_items, calories_consumed):
    log_path = f"data/{name}_logs.json"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    if os.path.exists(log_path):
        try:
            with open(log_path, "r") as file:
                users = json.load(file)
        except (json.JSONDecodeError, IOError):
            logs = {}
    else:
        logs = {}

    logs[self.date] = {
            "calories_consumed": calories_consumed,
            "food_items": food_items
        }
    
    try:
        with open(log_path, "w") as file:
            json.dump(logs, file, indent=4)
        print("Log saved successfully.")
    except IOError as e:
        print(f"Error saving log: {e}")
    

def load_logs(user):
    pass

