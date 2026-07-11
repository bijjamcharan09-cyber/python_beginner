from datetime import datetime

def load_expenses(filename="expenses.txt"):
    expenses = []

    try:
        with open(filename, "r") as file:
            for line in file:
                category, amount, date, time = line.strip().split(",")

                expenses.append({
                    "category": category,
                    "amount": float(amount),
                    "date": date,
                    "time": time
                })

    except FileNotFoundError:
        pass

    return expenses


def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']},{expense['date']},{expense['time']}\n")


def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    expenses.append({
        "category": category,
        "amount": amount,
        "date": date,
        "time": time
    })

    print("-------------")
    print("Expense added")
    print("-------------")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category:{expense['category']}\n   Amount:₹{expense['amount']:.2f}\n   Date:{expense['date']}\n   Time:{expense['time']}")
    print()


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ₹{total:.2f}\n")


def clear_expenses(expenses, filename="expenses.txt"):
    expenses.clear()
    open(filename, "w").close()
    print("All expenses have been cleared!\n")


def main():
    expenses = load_expenses()

    continue_choice = "yes"
    print("\t\t---------------")
    print("\t\tExpense Tracker")
    print("\t\t---------------")

    while continue_choice == "yes" or continue_choice == "1" or continue_choice == "y":
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Clear Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            clear_expenses(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.\n")

        if choice != "5":
            continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()

    if continue_choice not in ("yes", "1") and choice != "4":
        print("Goodbye!")


if __name__ == "__main__":
    main()