# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# define the variables
total_sum = 0
count = 0

# prompt user for input
while True:
    user_input = input("Input a number: ")

    try:
        number = float(user_input)
        total_sum += number
        count += 1
    except ValueError:
        break

# display the average if the numbers entered were valid