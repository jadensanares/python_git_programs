# Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Ask the user to input the first and second number
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Compare both of the numbers if they are equal
if number1 != number2:
    print("Not Equal")
else:
    print("Both numbers are equal.")