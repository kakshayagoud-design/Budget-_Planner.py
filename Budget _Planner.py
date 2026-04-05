# Budget Planner (Simple Version)

budget = 0
expenses = []

def set_budget(amount):
    global budget
    budget = amount

def add_expense(amount):
    expenses.append(amount)

def show_expenses():
    print("Expenses:", expenses)

def remaining_balance():
    return budget - sum(expenses)

# Main program
print("Budget Planner")

while True:
    print("\n1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Remaining Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter budget amount: "))
        set_budget(amount)

    elif choice == "2":
        amount = int(input("Enter expense amount: "))
        add_expense(amount)

    elif choice == "3":
        show_expenses()

    elif choice == "4":
        print("Remaining Balance:", remaining_balance())

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
