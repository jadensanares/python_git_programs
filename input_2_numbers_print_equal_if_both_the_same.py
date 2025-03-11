# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# tell the user to input 2 numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# calculate if both numbers are equal, if it is print equal
if number1 == number2:
    print("Both numbers are equal")
# use else statement if the result is not equal
else:
    print("Both numbers are not equal")