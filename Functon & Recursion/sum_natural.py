def sum_nat(a):
    if a == 1:
        return 1
    return a + sum_nat(a - 1)


n = int(input("Enter value of n: "))
print(f'Sum of {n} natural number is: {sum_nat(n)}')
