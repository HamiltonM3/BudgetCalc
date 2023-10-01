import math

#Welcome Message
print("Welcome to your Module 4 Budget")

#Write a program that asks the user to enter the amount that they have budgeted for a month. 

Budget = eval(input('Enter your budgeted amount for the month: '))

#A loop should then prompt the user to enter each of their expenses for the month and keep a running total. 

print("Your total budget for the month is: $", Budget)

Expenses = ["Housing", "Food", "Car", "Debt", "Entertainment", "Savings"]

print("Your expenses are: ", Expenses)

for i in Expenses:
    Costs = eval(input("Enter the actual cost for {}: ".format(i)))
    Budget -= Costs

#When the loop finishes, the program should display the amount that the user is over or under budget.

if Budget > 0:
    print("You are under your budget this month! You are under your budget by: $", Budget)
    
    
else:
    print("Oh no! You are over budget! You are over your budget by: $", Budget) 



