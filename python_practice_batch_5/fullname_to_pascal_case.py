# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# Example:
#Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

# Ask the user to input their full name in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# Convert the full name into Pascal Case
pascal_case = full_name.title().replace(" ", "")

# Print the result
print("The pascal casing of the input is:", pascal_case)