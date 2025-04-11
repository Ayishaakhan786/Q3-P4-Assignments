def print_divisors(num):
    # Print the divisors of the number
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")  # Print divisors in one line with space separation
    print()  # Print a new line after the divisors are printed

def main():
    num = int(input("Enter a number: "))  # Taking input from the user
    print_divisors(num)  # Calling the function to print divisors

# Calling the main function to run the program
main()