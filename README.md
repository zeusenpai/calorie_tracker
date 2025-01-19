# Calorie Tracker

A simple Python-based application to help users manage their calorie intake, track daily food consumption, and generate reports based on their fitness goals.

## Features

- **User Management**:
  - Add, update, and view user profiles.
  - Stores user details such as name, age, gender, height, weight, activity level, and fitness goals.
  
- **Calorie Calculations**:
  - Automatically calculates Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE).
  - Adjusts calorie recommendations based on the user's activity level and goals (e.g., lose, gain, or maintain weight).

- **Food Logging**:
  - Log daily food items with their calorie content.
  - Maintain a record of daily calorie consumption.

- **Daily Reports**:
  - View a summary of daily calorie intake, calorie balance, and TDEE.

## Prerequisites

- Python 3.7 or higher
- Required libraries:
  - `pandas`
  - `tabulate`
  - `json`
  - `os`
  - `datetime`

Install the required libraries with:

```bash
pip install pandas tabulate

