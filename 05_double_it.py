# Ask the user for a number
curr_value = int(input("Enter a number: "))

# Double the number until it reaches 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=" ")