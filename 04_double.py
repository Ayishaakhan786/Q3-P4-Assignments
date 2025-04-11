def double(num):
    # Multiply the given number by 2
    return num * 2

def main():
    # Prompt the user for a number
    num = int(input("Enter a number: "))
    
    # Call the double function and print the result
    result = double(num)
    print(f"Double that is {result}")

# Run the main function
if __name__ == "__main__":
    main()