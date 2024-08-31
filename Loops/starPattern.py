# Write a program to print the following star pattern.
#   *
#  ***
# *****

n = int(input('Enter value of n: '))

for i in range(1 , n+1):
    print(' '*(n-i))
    print(" * " * (2*i - 1))
