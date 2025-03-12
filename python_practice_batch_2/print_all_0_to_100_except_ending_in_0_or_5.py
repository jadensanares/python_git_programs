# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# Initialize a variable to start from 0
number = 0

# Use a while loop to iterate from 0 to 100 and check if it ends in 0 or 5
while number <= 100:
    if number % 10 != 0 and number % 10 != 5:
        print(number)
    
    number += 1
