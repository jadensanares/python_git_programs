# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# ask the user continously until input is invalid. Display highest number
highest_number = None

while True:
    user_input = input("Input a number:" )

    if user_input.strip() == "": # This is to check if the input is empty
        print("Highest Number:", highest_number)
        break
