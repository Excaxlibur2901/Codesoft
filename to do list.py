#Codesoft intern to do list program 

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added successfully.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            num = int(input("Enter task number to mark complete: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1] = tasks[num - 1] + " (Completed)"
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")