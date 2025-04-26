def sum_of_digits():
    #this function takes a number as input and returns the sum of its digits.
    # It takes an integer input from the user and calculates the sum of its digits using a loop.
    number = int(input("Enter a number: "))
    total = 0
    while number > 0:
        # This loop continues until the number becomes 0.
        # In each iteration, it extracts the last digit of the number and adds it to the total.
        digit = number % 10
        total += digit
        number //= 10
    print(f"Sum of digits: {total}")

sum_of_digits()
# Calling the function to execute it
