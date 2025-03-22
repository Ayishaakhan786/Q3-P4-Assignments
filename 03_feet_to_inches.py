INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    while True:
        try:
            feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
            inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
            print(f"That is {inches} inches!\n")
        except ValueError:
            print("Invalid input! Please enter a numerical value for feet.")

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()