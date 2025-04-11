def count_even(lst):
    # Counting the number of even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"The number of even numbers in the list is: {even_count}")

def main():
    lst = []
    while True:
        # Prompt user to enter an integer or press enter to stop
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":
            break  # Exit the loop if the user presses enter without entering anything
        
        try:
            num = int(user_input)  # Convert the input to an integer
            lst.append(num)  # Add the number to the list
        except ValueError:
            print("Please enter a valid integer.")
    
    count_even(lst)  # Call the function to count even numbers

# Running the main function
if __name__ == "__main__":
    main()