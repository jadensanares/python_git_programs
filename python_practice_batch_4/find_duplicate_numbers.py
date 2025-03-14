# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Initialize empty list to store numbers
numbers = []

# Prompt the user to input 10 numbers
for i in range(10):
    while True:
        try:
            # ask the user for a number
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break 
        except ValueError:
            print("Input invalid, Enter a valid integer.")

# Make a set to store duplicates
duplicates = set()

# Make a set to track see numbers
seen = set()

# look for duplicates
for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

# display results
if duplicates:
    print("Duplicate numbers are:", duplicates)
else:
    print("No duplicate numbers were found.")
