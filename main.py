import json
from datetime import datetime
import os

FILE_NAME = "expenses.json"


# Load expenses from JSON file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save expenses to JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add Expense
def add_expense(expenses):
    print("\n--- Add Expense ---")

    title = input("Enter expense title: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")

    expense = {
        "id": len(expenses) + 1,
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")


# View All Expenses
def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"{expense['title']} | "
            f"₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


# Total Expenses
def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total spent: ₹{total:.2f}")


# Category-wise Expenses
def category_expenses(expenses):
    print("\n--- Category-wise Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += expense["amount"]

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Search Expense
def search_expense(expenses):
    print("\n--- Search Expense ---")

    keyword = input("Enter title/category to search: ").lower()

    found = False

    for expense in expenses:
        if (
            keyword in expense["title"].lower()
            or keyword in expense["category"].lower()
        ):
            print(
                f"ID: {expense['id']} | "
                f"{expense['title']} | "
                f"₹{expense['amount']} | "
                f"{expense['category']} | "
                f"{expense['date']}"
            )
            found = True

    if not found:
        print("❌ No matching expense found.")


# Delete Expense
def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            print("✅ Expense deleted successfully!")
            return

    print("❌ Expense not found.")


# Main Program
def main():

    expenses = load_expenses()

    while True:

        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Expenses")
        print("5. Search Expense")
        print("6. Delete Expense")
        print("7. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_expenses(expenses)

        elif choice == "5":
            search_expense(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            print("👋 Thank you for using Expense Tracker!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()