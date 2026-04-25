tasks = []

while True:
    print("*" * 30)
    print("Welcome to the To-Do CLI")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Remove a task")
    print("4. Quit")
    print("*" * 30)

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("\nEnter a new task: ")
        tasks.append(task)
        print("*" * 30)
        print("Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            print("*" * 30)
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            print("*" * 30)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour tasks:")
            print("*" * 30)
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            print("*" * 30)

            index = input("Enter task number to delete: ")

            if index.isdigit():
                index = int(index)
                if 1 <= index <= len(tasks):
                    tasks.pop(index - 1)
                    print("Task deleted")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid option")
