# Define a new dictionary
my_dict = {
    'apple': 5,
    'banana': 8,
    'orange': 3
}

# Accessing elements
print(f"Number of apples: {my_dict['apple']}")  # Output: Number of apples: 5
print(f"Number of bananas: {my_dict['banana']}")  # Output: Number of bananas: 8

# Adding or updating an element
my_dict['grape'] = 10
print(f"After adding grapes: {my_dict}")
# Output: After adding grapes: {'apple': 5, 'banana': 8, 'orange': 3, 'grape': 10}

# Removing an element
removed_value = my_dict.pop('orange')
print(f"After removing oranges ({removed_value}): {my_dict}")
# Output: After removing oranges (3): {'apple': 5, 'banana': 8, 'grape': 10}

# Clear(): Removes all elements from the dictionary
my_dict.clear()
print(f"After clear(): {my_dict}")
# Output: After clear(): {}

# Copy(): Returns a shallow copy of the dictionary
original_dict = {'name': 'Bob', 'age': 25}
copied_dict = original_dict.copy()
print(f"Copied dictionary: {copied_dict}")
# Output: Copied dictionary: {'name': 'Bob', 'age': 25}

# keys(): Returns a view object that displays a list of all the keys in the dictionary
print(f"Keys: {original_dict.keys()}")
# Output: Keys: dict_keys(['name', 'age'])

# values(): Returns a view object that displays a list of all the values in the dictionary
print(f"Values: {original_dict.values()}")
# Output: Values: dict_values(['Bob', 25])

# items(): Returns a view object that displays a list of (key, value) tuple pairs
print(f"Items: {original_dict.items()}")
# Output: Items: dict_items([('name', 'Bob'), ('age', 25)])

# get(): Returns the value of the specified key, or a default value if the key does not exist
print(f"Age: {original_dict.get('age')}")
# Output: Age: 25

# update(): Updates the dictionary with the key-value pairs from another dictionary or iterable
original_dict.update({'city': 'San Francisco', 'gender': 'Male'})
print(f"After update: {original_dict}")
# Output: After update: {'name': 'Bob', 'age': 25, 'city': 'San Francisco', 'gender': 'Male'}

# popitem(): Removes and returns an arbitrary (key, value) pair from the dictionary
popped_item = original_dict.popitem()
print(f"Popped item: {popped_item}, Dictionary after popitem: {original_dict}")
# Output: Popped item: ('gender', 'Male'), Dictionary after popitem: {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
