# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter Number: "))
fact = 1

for i in range(2, num + 1):
    fact = fact * i

print(f"Factorial of {num} is: {fact}")