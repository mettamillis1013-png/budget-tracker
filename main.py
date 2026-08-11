#Personal Finance Tracker With Python will track your income and expenses, and provide you with a summary of your financial situation. It will allow you to input your income and expenses, categorize them, and generate reports to help you understand your spending habits.

print("Hello I am Your Personal Finance Tracker. I will help you manage your income and expenses effectively. Let's get started by entering your Name and financial data.")

print("Please enter your name:")
name = input()
print(f"Hello, {name}! Let's get started.")
print("Please enter your current pay rate (in dollars per hour):")
pay_rate = float(input())

print("Please enter the number of hours you work per day:")
hours_per_day = float(input())
print("Please enter the number of days you work per week:")
days_per_week = float(input())
hours_per_week = hours_per_day * days_per_week
hourly_income = pay_rate * hours_per_week

print(f"Your weekly income is: ${hourly_income:.2f}")
print(f"Your monthly income is: ${hourly_income * 4:.2f}")
print(f"Your yearly income is: ${hourly_income * 52:.2f}")

print("Please enter your expenses for the week (in dollars):")
expenses = float(input())

print("Please enter your expenses for the month (in dollars):")
monthly_expenses = float(input())

print(f"Your weekly expenses are: ${expenses:.2f}")
print(f"Your monthly expenses are: ${monthly_expenses:.2f}")
print(f"Your yearly expenses are: ${monthly_expenses * 12:.2f}")

weekly_savings = hourly_income - expenses
monthly_savings = (hourly_income * 4) - monthly_expenses

print(f"Your weekly savings are: ${weekly_savings:.2f}")
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your yearly savings are: ${monthly_savings * 12:.2f}")

print("Please enter your savings currently (in dollars):")
savings = float(input())

print("Please enter your financial goals (in dollars):")
financial_goals = float(input())

print(f"Your financial goals are: ${financial_goals:.2f}")