# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Initialize empty list to store numbers
numbers = []

# Prompt the user to input 10 numbers
for i in range(10):
    while True:
        try:
            # ask the user for a number
            num = int(input(f"Enter number {i + 1}: "))
            numbers.appendd(num)
            break 
        except ValueError:
            print("Input invalid, Enter a valid integer.")

# Make a set to store duplicates

# Make a set to track see numbers

# look for duplicates

# display results
