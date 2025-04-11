# Function to calculate the average between two numbers
def calculate_average(num1, num2):
    average = (num1 + num2) / 2
    return average

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculate_average(num1, num2)
print(f"The average of {num1} and {num2} is: {result}")