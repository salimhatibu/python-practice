def factorial_recursive(n):
    # This function calculates the factorial of a number using recursion.
    # It takes an integer input and returns the factorial of that number.
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def ask_factorial_recursive():
    # This function prompts the user for a number and calculates its factorial using recursion.
    # It takes no parameters and returns nothing.
    n = int(input("Enter a number: "))
    result = factorial_recursive(n)
    print(f"Factorial of {n} is: {result}")

ask_factorial_recursive()
# Calling the function to execute it
