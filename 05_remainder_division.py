def main():
    while True:
        try:
            # Get the numbers we want to divide
            dividend: int = int(input("Please enter an integer to be divided: "))
            divisor: int = int(input("Please enter an integer to divide by: "))
            
            # Ensure divisor is not zero
            if divisor == 0:
                print("Division by zero is not allowed. Please enter a valid divisor.")
                continue
            
            quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
            remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
            
            print(f"The result of this division is {quotient} with a remainder of {remainder}\n")
        except ValueError:
            print("Invalid input! Please enter integer values.")

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()