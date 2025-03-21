# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# Ask the user to input a complete statement
statement = input("Enter a complete statement: ")

# Word counter for the statement
word_counter = len(statement.split())

# Print result
print("Number of words in the statement:", word_counter)