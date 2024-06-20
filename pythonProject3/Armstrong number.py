def is_armstrong_number(number):
    # Convert the number to a string to easily access its digits
    num_str = str( number )
    # Calculate the number of digits in the number
    num_digits = len( num_str )
    # Initialize sum to 0
    armstrong_sum = 0

    # Iterate through each digit in the number
    for digit in num_str:
        # Convert the digit back to integer and raise it to the power of num_digits
        armstrong_sum += int( digit ) ** num_digits

    # Check if the sum equals the original number
    return armstrong_sum == number


# Example usage:
number = int( input( "Enter a number to check if it's an Armstrong number: " ) )
if is_armstrong_number( number ):
    print( number, "is an Armstrong number." )
else:
    print( number, "is not an Armstrong number." )