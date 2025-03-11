# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# tell the user to input 2 numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# make an if/else statement on determining the bigger number
if number1 > number2:
    print("The bigger number is", number1)
elif number2 > number1:
    print("The bigger number is", number2)

# print the result
else:
    print("Both numbers are equal.")