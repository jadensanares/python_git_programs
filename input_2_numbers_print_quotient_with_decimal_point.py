# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

# ask the user to input 2 numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# make the conditions for finding the quotient
if number2 == 0:
    print("Undefined")

else:
    quotient = number1 / number2
    print("The quotient is", quotient)