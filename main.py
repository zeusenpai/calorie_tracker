from models import *
from data_manager import *
import models
import pandas as pd

def add_user():
    print("------------------------")
    print("       Add User")
    print("------------------------")
    name = input("Name: ")
    age = int(input("Age: "))
    while True: 
        gender = input("Gender(M/F): ")
        if(gender.lower() == "m" or gender.lower() == "f"):
            break
        else:
            print("Invalid gender!")
            print()
    height = float(input("Height(in cm): "))
    weight = float(input("Weight(in kg): "))
    print()
        
    while True:
        print("Activity Level: \n1.Not Active\n2.Lightly Active\n3.Moderately Active\n4.Very Active\n5.Extremely Active")
        activity_level = int(input("Enter selection(1 - 5): "))
        if(activity_level < 1 or activity_level > 5):
            print("Invalid activity level!")
            print()
        else:
            break
    while True:
        print()
        print("Goal\n1.Lose Weight\n2.Gain Weight\n3.Maintain Weight")
        goal = int(input("Enter your selection: "))
        if(goal == 1 or 2 or 2):
            break
        else:
            print("Invalid Seleciton!")
            print()
    
    user = User(name, age, gender, height, weight, activity_level, goal)
    save_user(user)
    
def view_users():
    load_users()


while True:
    print("============================================")
    print("            CALORIE TRACKER")
    print("============================================")
    print("Main Menu:")
    print("1.Add a new user\n2.View all users\n3.Select a user\n4.Exit")
    ch = int(input("Select any options (from 1- 4): "))

    if(ch == 1):
        add_user()
    elif(ch == 2):
        view_users()
    elif(ch == 3):
        pass
    elif(ch == 4):
        break
    else:
        print("INVALID CHOICE!")
        print()

