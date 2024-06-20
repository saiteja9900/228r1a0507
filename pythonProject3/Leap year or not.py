def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter the year: "))
        if is_leap_year(year):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()