import random

# Randomly choose a number between 0 and 99
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

while True:
    try:
        guess = int(input("Enter a guess: "))

        if guess < secret_number:
            print("Your guess is too low\n")
        elif guess > secret_number:
            print("Your guess is too high\n")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break
    except ValueError:
        print("Please enter a valid number between 0 and 99.\n")