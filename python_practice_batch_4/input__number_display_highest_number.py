# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# ask the user continously until input is invalid. Display highest number
print("Input a number until it is invalid to display the highest number.")
highest_number = None

while True:
    user_input = input("Input a number:" )

    if user_input.strip() == "": # This is to check if the input is empty
        print("Highest Number:", highest_number)
        break

    try:
        user_input = int(user_input)
        if highest_number is None or user_input > highest_number:
            highest_number = user_input
    except ValueError:
        print("Highest Number:", highest_number)
        break