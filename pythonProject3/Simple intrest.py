def calculate_simple_interest(principal, rate, time):
    # Simple Interest Formula: SI = (P * R * T) / 100
    interest = (principal * rate * time) / 100
    return interest

def main():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the interest rate (in percentage): "))
        time = float(input("Enter the time period (in years): "))

        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest

        print("Simple Interest:", round(interest, 2))
        print("Total Amount:", round(total_amount, 2))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()