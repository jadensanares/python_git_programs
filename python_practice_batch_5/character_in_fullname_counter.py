# Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
# Example:
# Input: Juan Dela Cruz
# Output: 14

# Ask the user to input their full name
full_name = input("Enter your full name: ")

# Make the counter for the characters i full name
character_counter = len(full_name)

# Print Result
print("Number of characters in the input:", character_counter)