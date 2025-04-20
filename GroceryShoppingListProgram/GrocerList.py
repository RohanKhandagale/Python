# Grocery Shopping List using if-else and loops

shopping_list = []

print("Welcome to your Grocery Shopping List Manager!")

while True:
    print("\nWhat would you like to do?")
    print("1. Add an item")
    print("2. View list")
    print("3. Remove an item")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to your list.")

    elif choice == "2":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")

    elif choice == "3":
        if not shopping_list:
            print("Your shopping list is already empty.")
        else:
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
            to_remove = int(input("Enter the number of the item to remove: "))
            if 1 <= to_remove <= len(shopping_list):
                removed = shopping_list.pop(to_remove - 1)
                print(f"{removed} has been removed from your list.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please try again.")
