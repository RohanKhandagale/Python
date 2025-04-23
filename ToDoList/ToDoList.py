todo_list = []


def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if not todo_list:
            print("No tasks in your list.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list, start=1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index}. {task['task']} [{status}]")

    elif choice == "2":
        new_task = input("Enter your new task: ").strip()
        if new_task:
            todo_list.append({"task": new_task, "done": False})
            print(f"Task added: {new_task}")
        else:
            print("Task cannot be empty.")

    elif choice == "3":
        if not todo_list:
            print("No tasks to mark.")
        else:
            try:
                task_number = int(input("Enter task number to mark as done: "))
                if 1 <= task_number <= len(todo_list):
                    todo_list[task_number - 1]["done"] = True
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not todo_list:
            print("No tasks to remove.")
        else:
            try:
                task_number = int(input("Enter task number to remove: "))
                if 1 <= task_number <= len(todo_list):
                    removed = todo_list.pop(task_number - 1)
                    print(f"Removed task: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please pick from 1 to 5.")
