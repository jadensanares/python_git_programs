#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Initialize empty set to keep track of seen numbers
seen_numbers = set()

# Start loop to continue asking for input
while True:
    # Prompting the user to enter a number or type 'quit' to quit the program
    user_input = input("Enter a number (or type 'quit' to quit): ")

    # Check if the user wants to quit the program
    if user_input.lower() == 'quit':
        print("Quitting the program.")
        break  # EXITS THE LOOP
    
    # Converting input to an integer
    try:
        number = int(user_input)
    except ValueError:
        # If conversion fails, print message and continue
        print("Invalid input. Please enter a valid number.") 
        continue

    # Check if the number has been seen before
    if number in seen_numbers:
        print("Duplicate")
    else:
        print("Unique")
        seen_numbers.add(number)  # Add the number to the set of seen numbers
        