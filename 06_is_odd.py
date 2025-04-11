def check_even_odd():
    # Loop through numbers from 10 to 19
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

# Call the function to print even and odd numbers
check_even_odd()