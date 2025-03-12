# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Initialize a variable to keep track on the lowest number
lowest_number = None

# Make a loop to continue asking for input
while True:
# Prompt the user to enter a number
    user_input = input("Enter a number (or type 'quit' to quit): ")

# Creating an option for the user to quit the program
    if user_input.lower() == 'quit':
        break # Quitting the program when the user types 'quit'

# Converting input to integer
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Enter a valid number.")
        continue

# update the lowest number if there are changes with the valid input 
    if lowest_number is None or number < lowest_number:
        lowest_number = number

# after the loop, display the lowest number
if lowest_number is not None:
    print(f"The lowest number entered is: {lowest_number}")
else:
    print("No valid numbers were entered.")

# THE RESULT OF THE LOWEST NUMBER INPUT WILL DISPLAY AFTER THE USER HAS TYPED 'quit'