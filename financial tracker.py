import pandas as pd
import matplotlib.pyplot as plt

# This will hold your expense data
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

def add_expense():
    day = input("Enter day (1-31): ")
    month = input("Enter month (1-12): ")
    year = input("Enter year (e.g., 2025): ")
    date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"  # format date like 2025-11-24

    category = input("Enter category (e.g., Food, Transport): ")
    amount = input("Enter amount spent: ")

    # Convert amount to float and check input
    try:
        amount = float(amount)
    except:
        print("Invalid amount! Please try adding the expense again.")
        return

    global expenses
    # Add new expense row to the dataframe
    new = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    expenses = pd.concat([expenses, new], ignore_index=True)

    print(f"Added expense: {amount} INR for {category} on {date}")

def show_expenses():
    if expenses.empty:
        print("No expenses recorded yet!")
        return

    summary = expenses.groupby('Category').sum(numeric_only=True)
    print("\nExpenses summary by category:")
    print(summary)

    # Plot bar chart
    summary['Amount'].plot(kind='bar', color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount (INR)')
    plt.show()

print("Welcome to Simple Expense Tracker!")
while True:
    action = input("\nChoose action: (1) Add Expense, (2) Show Expenses, (3) Quit : ")
    if action == '1':
        add_expense()
    elif action == '2':
        show_expenses()
    elif action == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2 or 3.")
