def get_user_data():
    # Ask the user for their first name, last name, and email
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")

    # Return the collected data as a tuple
    return first_name, last_name, email

def main():
    # Call get_user_data() to get the user's information
    user_data = get_user_data()

    # Print the received user data as a tuple
    print("Received the following user data:", user_data)

# Call main() to run the program
main()