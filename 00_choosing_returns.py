# Define the constant for the adult age
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to the ADULT_AGE
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Ask the user for their age
    age = int(input("How old is this person?: "))
    # Call the function and print the result
    print(is_adult(age))

# Run the main function
main()