# Using various escape sequences in Python strings

# Newline (\n): Starts a new line
print("Hello\nWorld")
# Output:
# Hello
# World

# Tab (\t): Inserts a tab space
print("Hello\tWorld")
# Output: Hello    World

# Backslash (\\): Represents a literal backslash
print("This is a backslash: \\")
# Output: This is a backslash: \

# Single quote (\'): Represents a single quote character
print('She said, \'Hello!\'')
# Output: She said, 'Hello!'

# Double quote (\"): Represents a double quote character
print("He said, \"Hello!\"")
# Output: He said, "Hello!"

# Backspace (\b): Moves the cursor one character back
print("Hello\bWorld")
# Output: HellWorld

# Carriage return (\r): Moves the cursor to the beginning of the line
print("123\rABCD")
# Output: ABCD

# Octal (\ooo): Represents a character with the octal value ooo
print("\110\145\154\154\157")  # Octal values for "Hello"
# Output: Hello

# Hexadecimal (\xhh): Represents a character with the hexadecimal value hh
print("\x48\x65\x6c\x6c\x6f")  # Hexadecimal values for "Hello"
# Output: Hello

# Form feed (\f): Causes a page break or a new page on a printer (may not have visible effect in some environments)
print("Hello\fWorld")
# Output: Hello
#         World
