MIN_HEIGHT = 50  # Minimum height requirement

def check_height(height: int) -> None:
    """
    Checks if the given height meets the minimum height requirement.
    """
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def main():
    while True:
        user_input = input("How tall are you? (Press Enter to exit) ")
        
        if user_input == "":  # Exit condition
            print("Goodbye!")
            break
        
        try:
            height = int(user_input)  # Convert input to an integer
            check_height(height)  # Check if height meets the requirement
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
