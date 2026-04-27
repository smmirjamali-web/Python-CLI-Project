import json
import os

FILENAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                return []
    return []


def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()

while True:
    print("Welcome to the Expenses Calculator!")
    print("-" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Spending")
    print("4. Search By Category")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Title: ")
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount!")
            continue
        category = input("Category: ")
        expenses.append({
            "title": title,
            "amount": amount,
            "category": category
                        })
        save_expenses(expenses)
        print("Added Expense Successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses found!")
        else:
            for idx, e in enumerate(expenses, start=1):
                print(f"{idx}. Title: {e['title']}")
                print(f"    Amount: {e['amount']}")
                print(f"    Category: {e['category']}")
                print("-" * 40)

    elif choice == "3":
        total_spending = sum(expense["amount"] for expense in expenses)
        print(f"Total Spending: {total_spending}")
        print("-" * 40)

    elif choice == "4":
        cat = input("Enter your category: ")
        if not expenses:
            print("No expenses found!")
        found = False
        for expense in expenses:
            if expense["category"].lower() == cat.lower():
                print(f"{expense['title']}")
                found = True
                print("-" * 40)
        if not found:
            print("No expenses found in this category!")

    elif choice == "5":
        save_expenses(expenses)
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
