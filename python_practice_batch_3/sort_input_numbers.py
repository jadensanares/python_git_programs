# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# Initialize the empty list to store the numberss
numbers = []
# make a loop to cintue asking for input
while True:
# prompt the user to enter a number
    user_input = input("Enter a number: ")
# converting input to integer
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
# if conversion fails, print the sorted numbers and exit loop
        if numbers:
            numbers.sort()
            print("Numbers from lowest to highest:")
            print(numbers)
        else:
            print("Invalid numbers were entered.")
        break # exiting the loop after results have been displayed
