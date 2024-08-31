# Write a program to find out whether a given post is talking about “Harry” or not. No case-sensitive

msg = input("Enter your post: ")
search = input("Enter word to search: ")

# this search is for non-case-sensitive so we covert whole post and word in lowercase
if search.lower() in msg.lower():
    print("Word found")
else:
    print("word not found")

string = "hello"
print(string.upper())