def add_three_copies(lst: list, data) -> None:
    """
    Takes a list and a piece of data, then adds three copies of the data to the list.
    """
    for _ in range(3):
        lst.append(data)

def get_last_element(lst: list) -> None:
    """
    Prints the last element of the list.
    """
    print("Last element:", lst[-1])

def collect_user_values() -> list:
    """
    Continuously asks the user to enter values which are added one by one into a list.
    When the user presses enter without typing anything, the list is printed.
    """
    values = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    print("Here's the list:", values)
    return values

# There is no need to edit code beyond this point

def main():
    user_input: str = input("Enter a message to copy: ")  # Get user input
    my_list: list = []  # Create an empty list
    
    print("List before:", my_list)  # Print list before modification
    add_three_copies(my_list, user_input)  # Modify the list in-place
    print("List after:", my_list)  # Print list after modification
    
    get_last_element(my_list)  # Print the last element
    
    # Collect user values and print them
    collect_user_values()
    
if __name__ == '__main__':
    main()
