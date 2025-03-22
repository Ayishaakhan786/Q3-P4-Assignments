import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints the results
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {die1 + die2}")

def main():
    die1 = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")
    
    # Rolling the dice three times
    for _ in range(3):
        roll_dice()
    
    print(f"die1 in main() is still: {die1}")

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()