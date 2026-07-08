def load_expenses(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({"category": category, "amount": float(amount)})
    except FileNotFoundError:
        pass  
    return expenses


def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")


def add_expense(expenses):
    category = input("Enter category:")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("-------------\nExpense added\n-------------")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']:.2f}")
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
    print("\t\t---------------\n\t\tExpense Tracker\n\t\t---------------")

    while continue_choice == "yes" or continue_choice=="1":
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
        elif choice=="4":
            clear_expenses(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

        if choice != "5":
            continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()

    if (continue_choice != "yes" and continue_choice != "1")and choice != "4":
        print("Goodbye!")


if __name__ == "__main__":
    main()
