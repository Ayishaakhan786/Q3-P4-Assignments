def print_ones_digit(num):
    # Calculate the ones digit by using the modulo operator
    ones_digit = num % 10
    # Print the ones digit
    print(f"The ones digit is {ones_digit}")

def main():
    # Ask for user input
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

# Call the main function to run the program
main()