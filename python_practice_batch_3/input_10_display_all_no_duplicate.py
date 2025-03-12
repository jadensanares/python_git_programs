# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Initialize an empty list in able to store numbers
number_list = []
# Initialize an empty dictionary to count occurences of each number
number_count = {}

# Prompt user to input 10 numbers
for i in range(10):
    number = int(input(f"Enter the number {i + 1}: ")) # To get the user input
    number_list.append(number) # Adding number to list

    # Count the occurences of the number
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1

# Diplay the numbers that do not have duplicates
