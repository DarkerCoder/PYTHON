# Write a program to print multiplication table of n using for loops in reversed order

num = int(input("enter number: "))

print(f"Multiplication Table of {num} ==>")
for i in range(10, 0, -1):
    print(f"{num} * {i}  : {num * i} ")
