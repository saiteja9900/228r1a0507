def find_greatest_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def find_greatest_of_three(num1, num2, num3):
    greatest_of_two = find_greatest_of_two(num1, num2)
    return find_greatest_of_two(greatest_of_two, num3)

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        greatest_of_two = find_greatest_of_two(num1, num2)
        greatest_of_three = find_greatest_of_three(num1, num2, num3)

        print("The greatest of two numbers is:", greatest_of_two)
        print("The greatest of three numbers is:", greatest_of_three)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

