# Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide user with an option to look it up!

word = {"Takiya": "Pillow",
        "kursi": "Chair",
        "Madad": "Help",
        "Kitab": "Book",
        "Bhago": "Run"}

uttar = input("Enter your hindi word: ")
print(f"Translate in english of {uttar} is: {word.get(uttar)}")
