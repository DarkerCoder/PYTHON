# Write a program to sum a list with 4 numbers.
#  Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

list1 = [9, 4, 1, 2]
sum1 = sum(list1)
print(f'The sum of list is:', sum1)

a = (7, 0, 8, 0, 0, 9)
count_a = a.count(0)

print(f"Number of zeroes are: {count_a}")
