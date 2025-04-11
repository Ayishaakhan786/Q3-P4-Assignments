# Define the greet function
def greet(name):
    print(f"Greetings {name}!")

def main():
    # Ask the user for their name
    name = input("What's your name? ")
    # Call the greet function with the user's name
    greet(name)

# Run the main function
main()