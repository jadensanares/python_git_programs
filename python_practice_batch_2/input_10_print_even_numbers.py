# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Start the counter for even numbers
even_count = 0

# Ask the user to input 10 numbers 
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))

# Check if the number is even
    if number % 2 == 0:
            even_count += 1 

print("The total number of even numbers is:", even_count)
