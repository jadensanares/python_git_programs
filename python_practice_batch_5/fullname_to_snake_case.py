# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

# Ask the user to input their full name in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# Convert the full name into snake case
snake_case_name = full_name.lower().replace(" ", "_")

# Print the result
print("The name in snake case is:", snake_case_name)