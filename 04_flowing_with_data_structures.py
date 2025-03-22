def add_three_copies(lst: list, data) -> None:
    """
    Takes a list and a piece of data, then adds three copies of the data to the list.
    """
    for _ in range(3):
        lst.append(data)

# There is no need to edit code beyond this point

def main():
    user_input: str = input("Enter a message to copy: ")  # Get user input
    my_list: list = []  # Create an empty list
    
    print("List before:", my_list)  # Print list before modification
    add_three_copies(my_list, user_input)  # Modify the list in-place
    print("List after:", my_list)  # Print list after modification
    
if __name__ == '__main__':
    main()