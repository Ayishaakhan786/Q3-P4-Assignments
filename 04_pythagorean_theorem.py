import math  # Import the math library so we can use the sqrt function

def main():
    while True:
        try:
            # Get the two side lengths from the user and cast them to be numbers
            ab: float = float(input("Enter the length of AB: "))
            ac: float = float(input("Enter the length of AC: "))

            # Calculate the hypotenuse using the two sides and print it out
            bc: float = math.sqrt(ab**2 + ac**2)
            print(f"The length of BC (the hypotenuse) is: {bc}\n")
        except ValueError:
            print("Invalid input! Please enter numerical values for AB and AC.")

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()
