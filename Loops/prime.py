# Write a program to find whether a given number is prime or not.

num = int(input("Enter Number: "))
c = 0

for i in range(2, num):
    if num % i == 0:
        c += 1

if c == 0:
    print(f'{num} is a Prime Number')
else:
    print(f'{num} is not a prime Number')
