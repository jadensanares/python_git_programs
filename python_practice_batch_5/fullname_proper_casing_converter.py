# Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: Juan Dela Cruz

# Ask the user to input their full name
full_name = input("Enter your full name in incorrect casing: ")

# Convert the full name to proper casing
proper_casing_name = full_name.title()

# Print the result
print("Name:", proper_casing_name)