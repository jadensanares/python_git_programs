# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Start a list to store the numbers
numbers = []

# Ask the user to input 10 numbers
for i in range(10):
    number = int(input(f"Enter number {i + 1}: ")) 
    numbers.append(number) # Add the number to the list

# Calculate the result of the first number minus all of the remaining numbers
result = numbers [0]

# Subtract each of the remaining numbers from the result
print("The result of the first number minus all of the remaining numbers is:", result)
