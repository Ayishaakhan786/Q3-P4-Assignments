def subtract_seven(num):
    # Subtract 7 from num and return the result
    return num - 7

def main():
    # Prompt the user for a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print("The result after subtracting 7 is:", result)

# Call main() to run the program
main()