# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# Ask the user to input 2 numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Create the conditions then print the result
if number2 == 0:
    print("Cannot divide by zero.")

else:
    remainder = number1 % number2
    print("The remainder is", remainder)