# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Ask the user to input 2 numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Finding the smaller and larger number
start = min(number1, number2)  
end = max(number1, number2)

# Finding the numbers between the two
for number in range(start + 1, end):  
    print(number)