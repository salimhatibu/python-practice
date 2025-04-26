def sum_list():
    #this function takes a list of numbers as input and returns the sum of those numbers.
    list = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in list]
    total = 0
    #iterating through the list and adding each number to the total
    for num in numbers:
        total += num
    print(f"The sum is: {total}")

sum_list() #caling the function to execute it
