# Example 1: Using the walrus operator in a conditional statement
my_list = [1, 2, 3, 4, 5]
if (n := len(my_list)) > 5:
    print(f"List has {n} elements")
else:
    print(f"List has {n} elements, which is not greater than 5")

# Example 2: Using the walrus operator in a list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers if (n_squared := n**2) > 10]
print(squared_numbers)  # [16, 25]

# Example 3: Using the walrus operator in a lambda function
add_five = lambda x: (x_plus_five := x + 5)
print(add_five(10))  # 15