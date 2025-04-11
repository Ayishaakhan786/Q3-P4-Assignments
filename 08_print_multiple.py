def print_multiple(message, repeats):
    # Loop to print the message 'repeats' number of times
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")  # Taking user input for the message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Taking user input for the repeat count
    print_multiple(message, repeats)  # Calling the function to print the message multiple times

# Calling the main function to run the program
main()