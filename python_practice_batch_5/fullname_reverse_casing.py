# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz

# Ask the user to input their full name in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# Reverse the casing of each character using swapcase
reversed_casing_name = full_name.swapcase()

# Print the result
print("Output:", reversed_casing_name)
