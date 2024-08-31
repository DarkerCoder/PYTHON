# Write a program to print multiplication table of a given number using for loop.

num = int(input("enter number: "))

print(f"Multiplication Table of {num} ==>")
for i in range(10):
    print(f"{num} * {i+1}  10: {num*(i+1)}")

print()
num = int(input("enter number: "))
print(f"Multiplication Table of {num} ==>")
i = 1
while i <= 10:
    print(f"{num} * {i }  10: {num * i}")
    i += 1
