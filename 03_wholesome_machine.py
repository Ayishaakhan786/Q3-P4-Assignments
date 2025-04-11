# Target affirmation
affirmation = "I am capable of doing anything I put my mind to."

# Prompt the user until they type the correct affirmation
while True:
    print("Please type the following affirmation:")
    user_input = input()
    
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation.")