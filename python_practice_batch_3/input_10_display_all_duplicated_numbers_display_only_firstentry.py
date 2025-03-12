# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Initialize an empty list to store the numbers, Initialize an empty set to keep track of seen numbers
number_list = []
seen_numbers = set()
# Prompt the user input 10 numbers
for i in range(10):
    number = int(input(f"Enter a number {i + 1}: ")) # Getting the user input
    number_list.append(number) # Adding the number to the list

# Diplaying all numbers entered
print("All numbers entered:")
for number in number_list:
    print(number)

# Display the numbers showing duplicates only once
print("Numbers (duplicates shown only once):")
for number in number_list:
    if number not in seen_numbers: # Checking if the nubmer has not been seen
        print(number)
        seen_numbers.add(number) # Marking the number as seen