# Create an empty phonebook dictionary
phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        search_name = input("Enter name to search: ")
        if search_name in phonebook:
            print(f"{search_name}'s number is {phonebook[search_name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        print("\nPhonebook Contacts:")
        if not phonebook:
            print("No contacts saved yet.")
        else:
            for name, number in phonebook.items():
                print(f"{name}: {number}")

    elif choice == "4":
        print("Exiting Phonebook. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")