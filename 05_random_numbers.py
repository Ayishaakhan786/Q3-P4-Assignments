import random

def print_random_numbers():
    """
    Generates and prints 10 random numbers between 1 and 100.
    """
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(" ".join(map(str, random_numbers)))

if __name__ == '__main__':
    print_random_numbers()