# Dictionary with fruits and their prices
fruit_prices = {
    "apple": 10.5,
    "durian": 30,
    "jackfruit": 25,
    "kiwi": 15,
    "rambutan": 9,
    "mango": 12
}

total_cost = 0

# Loop through the dictionary
for fruit, price in fruit_prices.items():
    try:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price
    except ValueError:
        print("Please enter a valid number.")

# Display total
print(f"\nYour total is ${total_cost}")