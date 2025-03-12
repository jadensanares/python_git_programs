# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# ask the user continously until input is invalid. Display the number from highest to lowest
numbers = []

while True:
    user_input = input("Input a number: ")

    try: 
        nubmers = int(user_input)
        numbers.append(number)
    except ValueError:
        continue