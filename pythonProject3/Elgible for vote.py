def check_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote yet.")

def main():
    try:
        age = int(input("Please enter your age: "))
        check_eligibility(age)
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()