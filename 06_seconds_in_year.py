# Constants for time calculations
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate the number of seconds in a year
    seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result
    print("There are", seconds_in_year, "seconds in a year!")

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()
