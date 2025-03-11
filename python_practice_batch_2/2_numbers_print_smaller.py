# Create a program that ask user to input 2 numbers. Print the smaller number.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Compare the two numbers and print the bigger one
if number1 > number2:
    print("The smaller number is:", number2)
elif number2 > number1:
    print("The smaller number is:", number1)
else:
    print("Both of the numbers are equally the same.")
