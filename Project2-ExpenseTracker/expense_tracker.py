total = 0

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Total")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense = float(input("Enter expense amount: "))
        total = total + expense
        print("Expense Added Successfully!")

    elif choice == "2":
        print("Total Spent =", total)

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")