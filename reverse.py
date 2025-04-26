def reverse_string():
    # This function reverses a string without using built-in functions.
    # It takes a string input from the user and reverses it using a loop.
    s = input("Enter a string: ")
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    print(f"Reversed string: {reversed_str}")

reverse_string()
