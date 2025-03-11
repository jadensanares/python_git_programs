# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# define the sum
sum = 0


# make the conditions
for i in range(1, 11):
    number = int(input("Enter a number: "))
    sum += number

# print the result
print("The total sum is", sum)