#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
# Example:
# Input: 143
# Output: 000143

# Ask the user to input a number
number = int(input("Enter a number from (0-1000): "))

# For the number to 6 digits with leading zeroes
formatted_number = f"{number:06}"

# Print Result
print("Formatted Number:", formatted_number)