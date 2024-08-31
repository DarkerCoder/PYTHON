#Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word str which is a input by the user

# poem = input("Enter the poem:\n")
# with open("File/poem.txt","w") as f:
#     f.write(poem)

str = input("Enter the word you want to search: ")
with open("File/poem.txt", "r") as f:
    lines = f.read()
    if(str in lines):
        print(f"{str} is present in the poem.txt")
    else:
        print(f"{str} is not present in the poem.txt")

