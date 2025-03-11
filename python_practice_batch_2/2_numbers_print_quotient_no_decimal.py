# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# ask the user to input 2 numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# make the conditions and print the result
if number2 == 0:
    print("Error: Cannot divide by zero.")

else:
    quotient = number1 // number2
    print("The quotient of the two numbers is", quotient)