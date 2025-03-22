def get_first_element(lst: list) -> None:
    """
    Takes a list and prints the first element.
    """
    print("First element:", lst[0])

# There is no need to edit code beyond this point

def main():
    n: int = int(input("Enter the number of elements in the list: "))  # Get list size
    lst: list = []
    
    for _ in range(n):
        element = input("Enter an element: ")  # Get list elements from user
        lst.append(element)
    
    get_first_element(lst)  # Print first element
    
if __name__ == '__main__':
    main()