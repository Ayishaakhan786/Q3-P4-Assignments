# Initialize empty list
numbers = []

# Infinite loop to take input
while True:
    user_input = input("Enter a number (or press Enter to stop): ")
    
    # Break if input is empty
    if user_input == "":
        break
    
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Count occurrences using dictionary
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Print results
for num, count in count_dict.items():
    print(f"{num} appears {count} times.")