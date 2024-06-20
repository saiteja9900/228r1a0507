def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    try:
        number = int(input("Enter a number: "))
        result = check_even_odd(number)
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()