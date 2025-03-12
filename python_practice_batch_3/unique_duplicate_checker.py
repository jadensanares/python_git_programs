#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Initialize emty set to keep track of seen numbers
seen_numbers = set()

while True:
    user_input = input("Enter a number (or type 'quit' to quit): ")

    if user_input.lower() == 'quit':
        print("Quitting the program.")
        break
    
