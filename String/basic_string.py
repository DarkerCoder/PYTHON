# Define a string
s = "  Hello, World!  "

# len(): Returns the length of the string
print(f"Length of the string: {len(s)}")  # Output: Length of the string: 17

# str.upper() and str.lower(): Convert string to uppercase and lowercase
print(f"Uppercase: {s.upper()}")  # Output: Uppercase:    HELLO, WORLD!
print(f"Lowercase: {s.lower()}")  # Output: Lowercase:    hello, world!

# str.strip(): Remove leading and trailing whitespace
print(f"Stripped: '{s.strip()}'")  # Output: Stripped: 'Hello, World!'

# str.split(): Split the string into a list of substrings
print(f"Split: {s.split()}")  # Output: Split: ['Hello,', 'World!']

# str.join(): Join elements of a list into a string
words = ["Hello", "World"]
print(f"Joined: {' '.join(words)}")  # Output: Joined: Hello World

# str.find() and str.index(): Find the index of a substring
print(f"Index of 'World': {s.find('World')}")  # Output: Index of 'World': 10
print(f"Index of 'World': {s.index('World')}")  # Output: Index of 'World': 10

# str.replace(): Replace occurrences of a substring with another string
print(f"Replaced: {s.replace('Hello', 'Hi')}")  # Output: Replaced:    Hi, World!

# str.startswith() and str.endswith(): Check if string starts or ends with a substring
print(f"Starts with 'Hello': {s.startswith('Hello')}")  # Output: Starts with 'Hello': False
print(f"Ends with '!': {s.endswith('!')}")  # Output: Ends with '!': True

# str.isdigit(), str.isalpha(), str.isalnum(): Check if string consists of digits, alphabetical characters,
# alphanumeric characters
s1 = "123"
s2 = "abc"
s3 = "123abc"
print(f"{s1} is digit: {s1.isdigit()}")  # Output: 123 is digit: True
print(f"{s2} is alpha: {s2.isalpha()}")  # Output: abc is alpha: True
print(f"{s3} is alphanumeric: {s3.isalnum()}")  # Output: 123abc is alphanumeric: True

# str.format(): Format a string with placeholders
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice, and I am 30 years old.
