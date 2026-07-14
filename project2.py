# Project 2 - Expense Tracker

print("===== Expense Tracker =====")

total = 0

while True:
    expense = input("Enter expense amount (or type 'quit' to finish): ")

    if expense.lower() == "quit":
        break

    try:
        expense = int(expense)
        total = total + expense
        print("Current Total:", total)
    except ValueError:
        print("Invalid input! Please enter a number.")

print("\n===== Final Result =====")
print("Total Expenses =", total)
print("Thank you for using Expense Tracker!")