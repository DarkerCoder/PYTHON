word = input("Enter a word you want to change: ")
change = input("Enter in what string you want to change: ")

with open("File/don.txt","r") as f:
    content = f.read()
    contentNew = content.replace(word,change)

with open("File/don.txt","w") as f:
    f.write(contentNew)
