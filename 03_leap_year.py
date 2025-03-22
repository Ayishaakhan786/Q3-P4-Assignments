def is_leap_year(year: int) -> bool:
    """
    Determines whether a given year is a leap year based on the Gregorian calendar rules.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    year = int(input("Enter a year: "))
    
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()
