# Constant value for the maximum limit
MAX_VALUE = 10000

# Starting values of the Fibonacci sequence
a, b = 0, 1

# Print Fibonacci numbers while they are less than MAX_VALUE
while a < MAX_VALUE:
    print(a, end=" ")
    a, b = b, a + b