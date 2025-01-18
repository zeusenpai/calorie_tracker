from data_manager import *
from datetime import date

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
        if(self.gender.lower() == "m"):
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif(self.gender.lower() == "f"):
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        else:
            print("Error")
        return bmr
        
    
    def calculate_tdee(self):
        activity_multipliers = {
            1: 1.2,
            2: 1.375, 
            3: 1.55, 
            4: 1.725,  
            5: 1.9     
        }

        multiplier = activity_multipliers.get(self.activity_level)
        tdee = self.bmr * multiplier

        if self.goal == 1:
            tdee -= 500 
        elif self.goal == 2:
            tdee += 250
        elif(self.goal == 3):
            tdee = tdee
        
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
        save_logs(self, self.name, self.food_items, self.calories_consumed)

        print(f"Added '{food}' with {calories} kcal.")
        print(f"Total calories consumed today: {self.calories_consumed} kcal.")

    def add_activity(self):
        activity = input("Enter activity: ")
        burned = float(input("Enter calories burned: "))
        print(f"Activity Logged! Calories Burned: {burned}")
        return burned


