# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Make a loop for the continous asking for input
numbers = []
while True:
    user_input = input("Enter a number: ")

# Try to convert input to an integer
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        # The loop ends if input is invalid and show the result
        break

# Find the number with the most duplicates
most_duplicate_number = None
max_count = 0

for number in numbers:
    count = numbers.count(number)
    if count > max_count:
        max_count = count
        most_duplicate_number = number

# Display the number with the most number of duplicates
