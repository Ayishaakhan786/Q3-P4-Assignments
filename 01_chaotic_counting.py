import random

# Simulating the done() function with a random chance of returning True
DONE_LIKELIHOOD = 0.3  # 30% chance of being done

def done():
    # Returns True with a likelihood of DONE_LIKELIHOOD
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for i in range(1, 11):  # Loop from 1 to 10
        if done():
            return  # If done() returns True, exit the function
        print(i, end=" ")

def main():
    chaotic_counting()
    print("\nI'm done.")

# Running the main function
if __name__ == "__main__":
    main()