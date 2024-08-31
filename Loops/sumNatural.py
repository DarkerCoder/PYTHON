# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter number: "))
res = 0

i = 1
while i <= num:
    res = res + i
    i += 1

print(f"Sum of {num} Natural Number is : {res}")


