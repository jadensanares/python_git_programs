# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# define odd number
odd_number = 0

# make the equation
for i in range (1, 11):
    number = int(input("Enter a number: "))
    if number % 2 != 0:
        odd_number += 1

# print the result
print("Total:", odd_number)