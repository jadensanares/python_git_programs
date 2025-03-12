# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Initialize an empty list to store the numbers, Initialize an empty set to keep track of seen numbers
number_list = []
seend_numbers = set()
# Prompt the user input 10 numbers
for i in range(10):
    number = int(input(f"Enter a number {i + 1}: ")) # Getting the user input
    number_list.append(number) # Adding the number to the list

# Display the numbers showing duplicates only once
print("Numbers (duplicates shonw only once):")
