
# Dictionary to store contacts
contacts = {}

# Main Program Loop
while True:
    # Displaying the menu
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    # Taking user input for choice
    choice = input("Enter your choice: ")

    # Adding a new contact
    if choice == '1':
        name = input("Enter the contact name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")

        # Storing the contact
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact for {name} added successfully.")

    # Viewing a contact
    elif choice == '2':
        name = input("Enter the contact name to view: ")
        if name in contacts:
            print(f"\nName: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")

    # Deleting a contact
    elif choice == '3':
        name = input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print("Contact not found.")

    # Searching for a contact
    elif choice == '4':
        name = input("Enter the contact name to search: ")
        if name in contacts:
            print(f"\nName: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")

    # Displaying all contacts
    elif choice == '5':
        if len(contacts) > 0:
            print("\n--- All Contacts ---")
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
        else:
            print("No contacts available.")

    # Exiting the program
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break

    # If the user enters an invalid option
    else:
        print("Invalid choice, please try again.")
