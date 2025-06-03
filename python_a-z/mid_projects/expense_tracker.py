import csv
from datetime import datetime
def add_expense():
    try:
        date= input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount: "))
        with open('expenses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter the correct data format.")

def view_expenses():
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if not expenses:
                print("No expenses recorded.")
                return
            print(f"{'Date':<15} {'Category':<15} {'Description':<30} {'Amount':<10}")
            for expense in expenses:
                print(f"{expense[0]:<15} {expense[1]:<15} {expense[2]:<30} {expense[3]:<10}")
    except FileNotFoundError:
        print("No expenses recorded yet. Please add an expense first.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()