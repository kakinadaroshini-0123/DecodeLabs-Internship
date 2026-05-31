tasks = []

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            delete_task = int(input("Enter task number to delete: "))
            tasks.pop(delete_task - 1)

            print("Task Deleted Successfully!")

    elif choice == "4":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")