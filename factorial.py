def factorial_loop():
# This function calculates the factorial of a number using a loop.
    n = int(input("Enter a number: "))
    # Taking input from the user and converting it to an integer
    result = 1
    # Initializing result to 1
    for i in range(2, n + 1):
        result *= i
    print(f"Factorial of {n} is: {result}")

factorial_loop()
