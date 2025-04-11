# Define a dictionary to simulate Sophia's inventory
fruit_inventory = {
    "pear": 1000,
    "apple": 500,
    "banana": 300,
    "orange": 150,
    "grapes": 0,
    "kiwi": 0
}

# Function to check how many of a given fruit are in stock
def num_in_stock(fruit):
    """Returns the number of the given fruit in stock."""
    return fruit_inventory.get(fruit.lower(), 0)

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")

    # Get the number of fruits in stock using the function
    stock_count = num_in_stock(fruit)

    # Check if the fruit is in stock and print the appropriate message
    if stock_count > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock_count)
    else:
        print("This fruit is not in stock.")

# Call main() to run the program
main()