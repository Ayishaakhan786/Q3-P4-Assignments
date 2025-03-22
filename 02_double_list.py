def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes in a list of numbers and returns a new list with each element doubled.
    """
    return [num * 2 for num in numbers]

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers
    doubled_numbers: list[int] = double_numbers(numbers)  # Double each number
    print(doubled_numbers)  # Print out the doubled list
    
if __name__ == '__main__':
    main()